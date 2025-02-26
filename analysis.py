import re
from collections import defaultdict

MONTHS_EN_TO_CN = {
    "Jan": "1月", "Feb": "2月", "Mar": "3月", "Apr": "4月", "May": "5月", "Jun": "6月",
    "Jul": "7月", "Aug": "8月", "Sep": "9月", "Oct": "10月", "Nov": "11月", "Dec": "12月"
}

def parse_log(file_path):
    html_count = defaultdict(int)  # 统计 .html 访问量
    pwa_count = defaultdict(int)   # 统计 /pwa 访问量
    unique_ips = defaultdict(set)  # 统计唯一 IP 数量
    months_range = {}  # 记录每年出现的最早和最晚月份

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'^(\d+\.\d+\.\d+\.\d+).*\[(\d{2})/(\w{3})/(\d{4}):', line)
            if match:
                ip, day, month, year = match.groups()
                month_cn = MONTHS_EN_TO_CN.get(month, month)
                
                # 统计 IP 地址
                unique_ips[year].add(ip)
                
                # 统计 .html 访问量
                if '.html' in line:
                    html_count[year] += 1
                
                # 统计 /pwa 访问量
                if '/pwa' in line:
                    pwa_count[year] += 1
                
                # 记录每年的最早和最晚月份
                if year not in months_range:
                    months_range[year] = {month_cn}
                else:
                    months_range[year].add(month_cn)
    
    return html_count, pwa_count, {year: len(ips) for year, ips in unique_ips.items()}, months_range

def main():
    log_file = 'access.log'  # 你的 Nginx 日志文件路径
    html_stats, pwa_stats, ip_stats, months_range = parse_log(log_file)
    
    total_html = sum(html_stats.values())
    total_pwa = sum(pwa_stats.values())
    total_ips = sum(ip_stats.values())
    
    print("\n年度访问统计：")
    print("年度 | 网站访问量 | 移动应用访问量 | 访问用户数 | 记录时间段")
    print("------------------------------------------------------")
    for year in sorted(html_stats.keys() | pwa_stats.keys() | ip_stats.keys()):
        months = sorted(months_range.get(year, []), key=lambda m: list(MONTHS_EN_TO_CN.values()).index(m))
        month_range = f"{months[0]}-{months[-1]}" if months else "未知"
        print(f"{year} | {html_stats.get(year, 0):<10} | {pwa_stats.get(year, 0):<10} | {ip_stats.get(year, 0):<10} | {month_range}")
    
    print("------------------------------------------------------")
    print(f"合计   | {total_html:<10} | {total_pwa:<10} | {total_ips:<10} | 全部记录")

if __name__ == '__main__':
    main()
