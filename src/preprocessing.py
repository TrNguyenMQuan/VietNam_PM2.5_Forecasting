
def classify_region(city_name):
    north_west = ["Lai Châu", "Điện Biên Phủ", "Sơn La", "Lào Cai"]

    north_east = ["Cao Bằng", "Lạng Sơn", "Tuyên Quang", "Thái Nguyên"]

    north = ["Hà Nội", "Hải Phòng", "Hạ Long", "Bắc Ninh", "Hưng Yên", "Ninh Bình", "Việt Trì"]

    north_central = ["Thanh Hóa", "Vinh", "Hà Tĩnh", "Huế"]

    central_coast = ["Đà Nẵng", "Đông Hà", "Quảng Ngãi", "Nha Trang"]

    central_highland = ["Buôn Ma Thuột", "Pleiku", "Đà Lạt"]

    southern = ["Hồ Chí Minh", "Biên Hòa", "Tây Ninh", "Cao Lãnh", "Long Xuyên", "Cần Thơ", "Vĩnh Long", "Cà Mau"]

    if city_name in north_west:
        return "Tây Bắc"
    if city_name in north_east:
        return "Đông Bắc"
    if city_name in north:
        return "Bắc Bộ"
    if city_name in north_central:
        return "Bắc Trung Bộ"
    if city_name in central_coast:
        return "Nam Trung Bộ"
    if city_name in central_highland:
        return "Tây Nguyên"
    if city_name in southern:
        return "Nam Bộ"