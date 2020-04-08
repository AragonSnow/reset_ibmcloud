# reset_ibmcloud
基于IBMCloud cli的IBMCloud 重启脚本,放在vps上实现，实现无限白嫖IBMCloud，仅在Ubuntu 19上测试通过，其他平台自行测试

## 需要环境
Python3
IBMcloud CLI

## 使用
### 安装IBMcloud CLI 

```
sudo curl -sL https://ibm.biz/idt-installer | bash
ibmcloud config --check-version=false
```

### 复制程序
```
https://github.com/AragonSnow/reset_ibmcloud.git
```

### 修改配置
```
cp config.example.json config.json
```
修改成你的账号密码即可

### 修改文件路径
修改ibmcloud.py和api.py里面的路径 
```
hpath = "config文件路径"   修改成对应的config.json所在的路径
fp = codecs.open("日志文件路径", 'a', 'utf-8')    修改成要保存的日志文件路径
```


### 运行
```
python3  /path/to/ibmcloud.py
```
如果没有报错,可以查看上面的日志获取是否成功

### 添加计划任务
```
crontab -e
添加以下内容，每天3:22 AM 重启，时间可自定
 22  3  *   *   *    /usr/bin/python3  /path/to/ibmcloud.py   
```
