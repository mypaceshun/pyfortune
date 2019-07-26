from pyfortune.session import Session
import pandas as pd

class Search():

    """データ取得"""
    def __init__(self, username, password, group = None, number = None):
        s = Session()
        s.login(username, password)
        data_list = []
        flag = True
        page = 0
        while flag == True:
            add_data = s.fetch_apply_list(page)
            if not add_data:
                flag = False
            else:
                data_list.extend(add_data)
                page += 1
        link_list = pd.io.json.json_normalize(data_list)
        link_list = link_list[link_list["lottery_result"] != "落選"]
        link_list = link_list[link_list["lottery_result"] != "失効"]
        if group != None:
            if type(group) == str:
                link_list = link_list[link_list["event"].str.contains(group)]
            elif type(group) == list:
                link_list_ = link_list[link_list["event"].str.contains(group[0])]
                for i in range(len(group)):
                    add_list = link_list[link_list["event"].str.contains(group[i])]
                    link_list_ = pd.concat([link_list_, add_list])
                link_list = link_list_
                    
        if number != None:
            link_list = link_list[link_list["event"].str.contains(number)]
        
        
        detail_data = pd.DataFrame(columns = ["one_money", "subscription", "title", "title_left", "title_mid", "title_right", "total_money", "winning"], index = None)
        for link in link_list["link"]:
            add_list = pd.io.json.json_normalize(s.fetch_apply_detail(link))
            detail_data = pd.concat([detail_data,add_list])
        
        split_data = detail_data["title_mid"]
        split_data = split_data.str.split(" ", expand = True)
        split_data.columns = ["date", "place", "part"]
        data = pd.concat([detail_data[["one_money","subscription","title_left"]], split_data, detail_data[["title_right", "total_money", "winning"]]], axis = 1)
        data.columns = ["one_money", "subscription" , "member", "data", "venue", "part", "title", "total_money", "winning"]
        self.data = data


    """メンバー名で検索"""
    def search_member(self, data_list, member):
        search_member_data = data_list[data_list["member"] == member]
        return search_member_data


    """日付で検索"""
    def search_data(self, data_list, data):
        search_data_data = data_list[data_list["data"] == data]
        return search_data_data


    """会場で検索"""
    def search_venue(self, data_list, venue):
        search_venue_data = data_list[data_list["venue"] == venue]
        return search_venue_data


    """絞り込み検索 member:メンバー名 data:日にちx/x vetue:会場 指定がなければ検索しない ある条件での複数検索は不可(メンバー2人検索など)"""
    def search(self, member = None, data = None, venue = None):
        output_data = self.data
        if(member != None):
            output_data = self.search_member(output_data, member)
        if(data != None):
            output_data = self.search_data(output_data, data)
        if(venue != None):
            output_data = self.search_data(output_data, venue)
        return output_data

    
    """過去の枚数の累計"""
    def sum_sheets(self, member):
        data = self.search(member)
        return data["winning"].sum()

    
    """過去行ったことあるメンバーと枚数一覧取得"""
    def past_member(self, group = None):
        data = self.search()
        if(group != None):
            link_list = link_list[link_list["title"].str.contains(group)]
        member_list = self.data[~self.data["member"].duplicated()]["member"]
        
        output = []
        for mem in member_list:
            sum_data = data[data["member"] == mem]
            output.append([mem, sum_data["winning"].sum()])
        
        output = pd.DataFrame(output)
        output.columns = ["member", "winning"]
        output = output.sort_values(by=["winning"], ascending = False)
        return output