import requests,csv,json,time

def read():
	name = []
	acc = []
	#打开配置文件
	with open('amm.csv','r') as myFile:
	    lines=csv.reader(myFile)
	    #得到每人的数据
	    for line in lines:
	        name.append(line[1])
	        #姓名
	        acc.append(line[3])
	        #账号
	del name[0]
	del acc[0]
	#删除两者第一个标签，保留数据
	return(name,acc)

def write(rows):
	with open('成绩.csv','w',newline='') as f:
		f_csv = csv.writer(f)
		f_csv.writerows(rows)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:78.0) Gecko/20100101 Firefox/78.0'}
def login(acc):
    data = {'loginName' : acc, 'password' : '1q2w3e123', 'rememberMe' : '1', 'roleType' : '1'}
    get_cookies = requests.post('https://hfs-be.yunxiao.com/v2/users/sessions',data = data, headers = headers)
    res = requests.get('https://hfs-be.yunxiao.com/v3/exam/list?start=-1', headers = headers, cookies = get_cookies.cookies)
    return res

def main():
	#获取名字
	name = read()[0]
	#获取账号
	acc = read()[1]
	#初始化
	first = []
	ii = 0
	for i in acc:
		text = json.loads(login(i).text)
		secend = []
		#筛取分数
		score = str(text['data']['list'][0]['score'])
		secend.append(name[ii])
		secend.append(score)
		first.append(secend)
		print(name[ii] + ':' + score)
		ii += 1
	choose = input('爬取成功！是否打印成表格？\n（输入‘1’打印，否则回车退出)\n:')
	if choose == '1':
		write(first)
	time.sleep(2)
	print('已在当前目录生成表格！')
	time.sleep(3)

main()
