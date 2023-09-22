def string_to_cookie_dict(text: str) -> dict:
    items: list = text.split("; ")
    return_dict: dict = {}
    for item in items:
        key: str = item.split("=")[0]
        value: str = item.split("=")[1]
        return_dict[key] = value
    return return_dict

if __name__ == "__main__":
    text: str = "sdc_session=1695267753233; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1695267753; _jzqc=1; _jzqckmp=1; __utmc=63332592; __utmz=63332592.1695267755.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ck_RegFromUrl=https%3A//live.500.com/2h1.php; _jzqa=1.1423380480098453000.1695267754.1695342797.1695344994.9; _jzqx=1.1695270204.1695344994.1.jzqsr=live%2E500%2Ecom|jzqct=/2h1%2Ephp.-; _qzjc=1; __utma=63332592.1799054545.1695267755.1695342799.1695344996.9; WT_FPC=id=undefined:lv=1695345614170:ss=1695344992625; sdc_userflag=1695344992627::1695345614173::2; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1695345614; _qzja=1.1274752972.1695267754158.1695342797391.1695344994083.1695344994083.1695345614253.0.0.0.24.9; _qzjb=1.1695344994083.2.0.0.0; _qzjto=4.2.0; _jzqb=1.2.10.1695344994.1; __utmb=63332592.2.10.1695344996; motion_id=1695345618049_0.7319330353398945; CLICKSTRN_ID=106.83.118.195-1695267753.399065::2331A0CAA1D65F02DE32F374EF982B94; tgw_l7_route=1708f7089570919168107aecc592756d"
    print(string_to_cookie_dict(text=text))