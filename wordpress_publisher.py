#coding:utf-8
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
 
username = 'username'
password = 'password'
site = 'wordpresssite/xmlrpc.php'
wp = Client(site, username, password)

post = WordPressPost()
post.title = 'TEST'
post.content = 'Hello World'
post.id = wp.call(posts.NewPost(post))
post.post_status = 'publish'
wp.call(posts.EditPost(post.id, post))
 
# post = WordPressPost()
# post.title = 'Title'
# post.content = 'Hello World'
# post.post_status = 'publish' #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
# post.terms_names = {
	# 'post_tag': ['python', 'xmlrpc'], #文章所属标签，没有则自动创建
	# 'category': ['python', 'xmlrpc'] #文章所属分类，没有则自动创建
 # }
 
# post.custom_fields = []   #自定义字段列表
# post.custom_fields.append({  #添加一个自定义字段
        # 'key': 'price',
        # 'value': 0
# })
# post.custom_fields.append({ #添加第二个自定义字段
        # 'key': 'address',
        # 'value': '天涯海角'
# })

# post.date = datetime.strptime('2020-03-30', '%Y-%m-%d') # 发布时间
# post.thumbnail = 11 #缩略图的id
# post.id = wp.call(posts.NewPost(post))
