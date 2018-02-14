通过之前课程设计，发现Java开发Web的程序臃肿，感觉不太适合我们课程设计这种小项目，改一个功能改好多文件，到最后改的好繁琐，导致我们都不想加新功能了。
之前零零散散看来下Python方面的知识，最近假期期间又零零散散的看了不少，发现看的越多不懂的也越多:flushed:，不想看了，准备把之前的课程设计用Flask框架弄一遍，方便以后愉快地复制粘贴。

----------

最近看的一些书籍：
- 《Flask Web开发:基于Python的Web应用开发实战》  
一句感慨，这开发Web也太方便了吧。   
- 《Python进阶》  
加强对于Python的理解，这本书把一些常用的Python知识说了下
- 《Python Cookbook（第三版）》  
嗯，这本书有一定难度，详细的介绍了Python3的一些秘籍，看了前十章，有些地方都看的心态崩了，感觉这本书对于加强python是必不可少的，立个flag,以后重点看看。

----------
### 遇到一些问题
- 之前基于Java的静态文件如a.css直接写css/a.css,但在flask里面要改成static/css/a.css，不想改HTML的代码，查了好久，没查到什么好的方法，突然想到重定向（聪明） 
 ``` 
	static_file_suffix = ['.css', '.png']
	@login.before_app_request
	def static_file():
    if request.endpoint != 'static':
        path = request.path
        if path[path.rfind('.'):] in static_file_suffix:
            return redirect('static' + request.path)
 ```
- 每个蓝图比如`@student.before_request`只拦截已经定义的路径，不存在的路径是直接返回404的，不会进入该方法
- flask-login加载用户，由于不同用户涉及到不同表的访问，实现的`get_id`方法要返回表和`id`
 ``` 
    def get_id(self):
    return self.__tablename__, self.id

	table_dict = {'student': Student, 'teacher': Teacher, 'admin': Admin}

    @login_manager.user_loader
    def load_user(user_id):
    tablename, id = user_id
    return table_dict[tablename].query.get(id)
  ```
一开始不明白为什么文档里面每次请求都从数据库中加载用户，这样性能会降低， 查了下，发现是为了安全，比如用户打开了两个session，在一个session里面用户修改了密码，提交到数据库，那另外一个session加载用户时发现密码被修改了可以强制退出，个人想到的实现方法是每个session记录登进来的密码，每次请求都与数据库中加载用户的密码对比，不相等就退出
- flask上传文件的问题，本来是想跟springmvc那样自动搞个临时文件，结果查了一下午没有什么好的解决方法，于是乎先保存文件再手动删除，再次吐槽python的自动补齐（毕竟用惯了Java）。