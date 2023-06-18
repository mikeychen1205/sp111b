# 創建一個 Context 類來表示上下文層：
class Context:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.containers = []
    
    def add_container(self, container):
        self.containers.append(container)

# 創建 Container 和 Component 類來表示容器層和元件層：
class Container:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)

class Component:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# 創建上下文
context = Context("My App", "Description of my app")

# 創建容器
web_app = Container("Web App", "Web application container")
database = Container("Database", "Database container")

# 創建元件
login_component = Component("Login", "User login component")
dashboard_component = Component("Dashboard", "Main dashboard component")

# 將容器和元件添加到上下文
context.add_container(web_app)
context.add_container(database)

web_app.add_component(login_component)
web_app.add_component(dashboard_component)
