#!/usr/bin/env python

# This is a simple web server for a traffic counting application.
#这是用于流量统计应用程序的简单Web服务器。
# It's your job to extend it by adding the backend functionality to support
# recording the traffic in a SQL database. You will also need to support
# some predefined users and access/session control.
#通过添加后端功能来扩展它以支持在SQL数据库中记录流量，这是您的工作。
#您还需要支持一些预定义的用户和访问/会话控制。

#You should only need to extend this file. The client side code (html, javascript and css)
# is complete and does not require editing or detailed understanding.
#您只需要扩展此文件。 客户端代码（html，javascript和css）是完整的，不需要进行编辑或详细了解。



# import the various libraries needed
import http.cookies as Cookie # some cookie handling support
from http.server import BaseHTTPRequestHandler, HTTPServer # the heavy lifting of the web server
import urllib # some url parsing support
import base64 # some encoding support

# This function builds a refill action that allows part of the
# currently loaded page to be replaced.
#此功能建立一个重新填充操作，该操作允许替换当前加载页面的一部分。
def build_response_refill(where, what):
    text = "<action>\n"
    text += "<type>refill</type>\n"
    text += "<where>"+where+"</where>\n"
    m = base64.b64encode(bytes(what, 'ascii'))
    text += "<what>"+str(m, 'ascii')+"</what>\n"
    text += "</action>\n"
    return text


# This function builds the page redirection action
# 此功能可建立页面重定向动作
# It indicates which page the client should fetch.
# 指示客户端应提取哪个页面。
# If this action is used, only one instance of it should
# 如果使用此操作，则应仅执行该操作的一个实例
# contained in the response and there should be no refill action.
# 包含在响应中，不应执行重新填充操作。
def build_response_redirect(where):
    text = "<action>\n"
    text += "<type>redirect</type>\n"
    text += "<where>"+where+"</where>\n"
    text += "</action>\n"
    return text

## Decide if the combination of user and magic is valid
#确定user和magic的组合是否有效
def handle_validate(iuser, imagic):
    if (iuser == 'test') and (imagic == '1234567890'):
        return True
    else:
        return False

## remove the combination of user and magic from the data base, ending the login
#从数据库中删除用户和魔术的组合，结束登录
def handle_delete_session(iuser, imagic):
    return

## A user has supplied a username (parameters['usernameinput'][0])
## and password (parameters['passwordinput'][0]) check if these are
## valid and if so, create a suitable session record in the database
## with a random magic identifier that is returned.

#用户提供了用户名（参数['usernameinput'] [0]）和密码（参数['passwordinput'] [0]）
#检查它们是否有效，如果有效，则在数据库中创建一个合适的会话记录，并返回一个随机魔术标识符。

## Return the username, magic identifier and the response action set.
#返回用户名，魔术标识符和响应操作集。
def handle_login_request(iuser, imagic, parameters):
    if handle_validate(iuser, imagic) == True:
        # the user is already logged in, so end the existing session.
        #用户已经登录，因此结束现有会话。
        handle_delete_session(iuser, imagic)

    text = "<response>\n"
    if parameters['usernameinput'][0] == 'test': ## The user is valid
        text += build_response_redirect('/page.html')
        user = 'test'
        magic = '1234567890'
    else: ## The user is not valid
        text += build_response_refill('message', 'Invalid password')
        user = '!'
        magic = ''
    text += "</response>\n"
    return [user, magic, text]

# text?  parameters['passwordinput'][0]?


## The user has requested a vehicle be added to the count
#用户已请求将车辆添加到计数中
## parameters['locationinput'][0] the location to be recorded 要记录的位置
## parameters['occupancyinput'][0] the occupant count to be recorded 要记录的人数
## parameters['typeinput'][0] the type to be recorded 要记录的类型
## Return the username, magic identifier (these can be empty  strings) and the response action set.
def handle_add_request(iuser, imagic, parameters):
    text = "<response>\n"
    if handle_validate(iuser, imagic) != True:
        #Invalid sessions redirect to login - 无效的会话重定向到登录
        text += build_response_redirect('/index.html')
    else: ## a valid session so process the addition of the entry.
        #有效的会话，因此请处理条目的添加。
        text += build_response_refill('message', 'Entry added.') #替换一部分：条目已添加
        text += build_response_refill('total', '0')
    text += "</response>\n"
    user = ''
    magic = ''
    return [user, magic, text]

## The user has requested a vehicle be removed from the count
# 用户已要求将车辆从计数中删除
## This is intended to allow counters to correct errors.
# 允许计数器纠正错误
## parameters['locationinput'][0] the location to be recorded 要记录的位置
## parameters['occupancyinput'][0] the occupant count to be recorded 要记录的人数
## parameters['typeinput'][0] the type to be recorded 要记录的类型
## Return the username, magic identifier (these can be empty  strings) and the response action set.
def handle_undo_request(iuser, imagic, parameters):
    text = "<response>\n"
    if handle_validate(iuser, imagic) != True:
        #Invalid sessions redirect to login - 无效的会话重定向到登录
        text += build_response_redirect('/index.html')
    else: ## a valid session so process the recording of the entry.
        text += build_response_refill('message', 'Entry Un-done.') #替换一部分：输入未完成
        text += build_response_refill('total', '0')
    text += "</response>\n"
    user = ''
    magic = ''
    return [user, magic, text]

# This code handles the selection of the back button on the record form (page.html)
# 此代码处理记录表单（page.html）上的后退按钮的选择
# You will only need to modify this code if you make changes elsewhere that break its behaviour
# 仅当您在其他地方进行更改以破坏其行为时，才需要修改此代码
def handle_back_request(iuser, imagic, parameters):
    text = "<response>\n"
    if handle_validate(iuser, imagic) != True:
        text += build_response_redirect('/index.html')
    else:
        text += build_response_redirect('/summary.html')
    text += "</response>\n"
    user = ''
    magic = ''
    return [user, magic, text]

## This code handles the selection of the logout button on the summary page (summary.html)
# 此代码处理摘要页面（summary.html）上的注销按钮的选择
## You will need to ensure the end of the session is recorded in the database
# 您需要确保会话结束记录在数据库中
## And that the session magic is revoked.
# 会话魔术被撤销。
def handle_logout_request(iuser, imagic, parameters):
    text = "<response>\n"
    text += build_response_redirect('/index.html') #注销后跳转到登录界面
    user = '!'
    magic = ''
    text += "</response>\n"
    return [user, magic, text]

## This code handles a request for update to the session summary values.
# 该代码处理更新会话summary values的请求
## You will need to extract this information from the database.
# 您将需要从数据库中提取此信息
def handle_summary_request(iuser, imagic, parameters):
    text = "<response>\n"
    if handle_validate(iuser, imagic) != True:
        text += build_response_redirect('/index.html')
    else:
        text += build_response_refill('sum_car', '0') #？0是什么
        text += build_response_refill('sum_taxi', '0')
        text += build_response_refill('sum_bus', '0')
        text += build_response_refill('sum_motorbike', '0')
        text += build_response_refill('sum_bicycle', '0')
        text += build_response_refill('sum_van', '0')
        text += build_response_refill('sum_truck', '0')
        text += build_response_refill('sum_other', '0')
        text += build_response_refill('total', '0')
        text += "</response>\n"
        user = ''
        magic = ''
    return [user, magic, text]
#？？？

# HTTPRequestHandler class
class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET This function responds to GET requests to the web server.
    def do_GET(self):

        # The set_cookies function adds/updates two cookies returned with a webpage.
        # These identify the user who is logged in. The first parameter identifies the user
        # and the second should be used to verify the login session.
        def set_cookies(x, user, magic):
            ucookie = Cookie.SimpleCookie()
            ucookie['u_cookie'] = user
            x.send_header("Set-Cookie", ucookie.output(header='', sep=''))
            mcookie = Cookie.SimpleCookie()
            mcookie['m_cookie'] = magic
            x.send_header("Set-Cookie", mcookie.output(header='', sep=''))

        # The get_cookies function returns the values of the user and magic cookies if they exist
        # it returns empty strings if they do not.
        def get_cookies(source):
            rcookies = Cookie.SimpleCookie(source.headers.get('Cookie'))
            user = ''
            magic = ''
            for keyc, valuec in rcookies.items():
                if keyc == 'u_cookie':
                    user = valuec.value
                if keyc == 'm_cookie':
                    magic = valuec.value
            return [user, magic]

        # Fetch the cookies that arrived with the GET request
        # The identify the user session.
        user_magic = get_cookies(self)

        print(user_magic)

        # Parse the GET request to identify the file requested and the GET parameters
        parsed_path = urllib.parse.urlparse(self.path)

        # Decided what to do based on the file requested.

        # Return a CSS (Cascading Style Sheet) file.
        # These tell the web client how the page should appear.
        if self.path.startswith('/css'):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('.'+self.path, 'rb') as file:
                self.wfile.write(file.read())
            file.close()

        # Return a Javascript file.
        # These tell contain code that the web client can execute.
        if self.path.startswith('/js'):
            self.send_response(200)
            self.send_header('Content-type', 'text/js')
            self.end_headers()
            with open('.'+self.path, 'rb') as file:
                self.wfile.write(file.read())
            file.close()

        # A special case of '/' means return the index.html (homepage)
        # of a website
        elif parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('./index.html', 'rb') as file:
                self.wfile.write(file.read())
            file.close()

        # Return html pages.
        elif parsed_path.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('.'+parsed_path.path, 'rb') as file:
                self.wfile.write(file.read())
            file.close()

        # The special file 'action' is not a real file, it indicates an action
        # we wish the server to execute.
        elif parsed_path.path == '/action':
            self.send_response(200) #respond that this is a valid page request
            # extract the parameters from the GET request.
            # These are passed to the handlers.
            parameters = urllib.parse.parse_qs(parsed_path.query)

            if 'command' in parameters:
                # check if one of the parameters was 'command'
                # If it is, identify which command and call the appropriate handler function.
                if parameters['command'][0] == 'login':
                    [user, magic, text] = handle_login_request(user_magic[0], user_magic[1], parameters)
                    #The result to a login attempt will be to set
                    #the cookies to identify the session.
                    #尝试登录的结果将是设置cookie以标识会话。
                    set_cookies(self, user, magic)
                elif parameters['command'][0] == 'add':
                    [user, magic, text] = handle_add_request(user_magic[0], user_magic[1], parameters)
                    if user == '!': # Check if we've been tasked with discarding the cookies.
                        set_cookies(self, '', '')
                elif parameters['command'][0] == 'undo':
                    [user, magic, text] = handle_undo_request(user_magic[0], user_magic[1], parameters)
                    if user == '!': # Check if we've been tasked with discarding the cookies.
                        set_cookies(self, '', '')
                elif parameters['command'][0] == 'back':
                    [user, magic, text] = handle_back_request(user_magic[0], user_magic[1], parameters)
                    if user == '!': # Check if we've been tasked with discarding the cookies.
                        set_cookies(self, '', '')
                elif parameters['command'][0] == 'summary':
                    [user, magic, text] = handle_summary_request(user_magic[0], user_magic[1], parameters)
                    if user == '!': # Check if we've been tasked with discarding the cookies.
                        set_cookies(self, '', '')
                elif parameters['command'][0] == 'logout':
                    [user, magic, text] = handle_logout_request(user_magic[0], user_magic[1], parameters)
                    if user == '!': # Check if we've been tasked with discarding the cookies.
                        set_cookies(self, '', '')
                else:
                    # The command was not recognised, report that to the user.
                    # 无法识别该命令，将其报告给用户。
                    text = "<response>\n"
                    text += build_response_refill('message', 'Internal Error: Command not recognised.')
                    text += "</response>\n"

            else:
                # There was no command present, report that to the user.
                # 目前没有命令，请向用户报告。
                text = "<response>\n"
                text += build_response_refill('message', 'Internal Error: Command not found.')
                text += "</response>\n"
                self.send_header('Content-type', 'application/xml')
                self.end_headers()
                self.wfile.write(bytes(text, 'utf-8'))
        else:
            # A file that doesn't fit one of the patterns above was requested.
            # 请求的文件不符合上述模式之一。
            self.send_response(404)
            self.end_headers()
        return

# This is the entry point function to this code.
def run():
    print('starting server...')
    ## You can add any extra start up code here
    # Server settings
    # Choose port 8081 over port 80, which is normally used for a http server
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever() # This function will not return till the server is aborted.

run()
