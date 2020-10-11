import requests, re, xlrd

file = xlrd.open_workbook("配置文件.xlsx")
t = file.sheets()[0]
nrows = t.nrows
def excel():
    dict = {}
    for i in range(1, nrows):
        dict[i] = t.row_values(i)
        #形成一个n:n行数据的字典
    return dict
#获得一个工作表的所有行的数据

def login_score(name):
    data = {'loginName' : name, 'password' : '1q2w3e123', 'rememberMe' : '1', 'roleType' : '1'}
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:78.0) Gecko/20100101 Firefox/78.0'}

    a = requests.post('https://hfs-be.yunxiao.com/v2/users/sessions',data = data, headers = headers)
    res = requests.get('https://hfs-be.yunxiao.com/v2/exam/trends-overview',data = data, headers = headers, cookies = a.cookies)
    return res
#得到总成绩的text数据

def login_each_score(code_ID, name):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:78.0) Gecko/20100101 Firefox/78.0'}

    data = {'loginName' : name, 'password' : '1q2w3e123', 'rememberMe' : '1', 'roleType' : '1'}
    a = requests.post('https://hfs-be.yunxiao.com/v2/users/sessions',data = data, headers = headers)
    url_each_score = requests.get('https://hfs-be.yunxiao.com/v2/exam/%s/overview' %code_ID, headers = headers, cookies = a.cookies)
    return url_each_score
#提取每个账号的各科成绩text数据


def main():
    print('等待网络响应')
    for i in range(1,nrows):
        url = eval(login_score(excel()[i][3]).text)
            #获得每个账号的成绩数据
        code_ID = url['data'][0]['examId']
            #获得每个账号考试ID
        url_score = url['data'][0]['score']
            #处理每个账号的总成绩数据
        meum = {}
        meum[excel()[i][1]] = url_score
        #将总成绩 ....................... 变成字典形式放入列表
        print(meum)
        #打印最终得到的总数据
    input('爬取完成！')

main()
