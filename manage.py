#书上的部分：应用主脚本
import os
# 从应用包的构造文件中引入create_app
from App import create_app
# 引入flask-migrate
from flask_migrate import MigrateCommand
# 引入flask-script
from flask_script import Manager
from  flask_apscheduler import APScheduler
class Config(object):
    JOBS=[
        {
            'id':'job1',
            'func':'__main__:job_1',
            'trigger':'interval',
            'seconds':5
        }
    ]



# python中os模块获取环境变量的一个方法，FLASK_ ENV为flask中内置的配置变量
env = os.environ.get("FLASK_ ENV", "develop")
# 创建一个app
app = create_app(env)
app.config.from_object(Config())
# 使用Manager实例调用script命令
manager = Manager(app)
# flask-migrate也支持flask-script的命令行接口，所以可以用flask-script统一管理，
# flask-migrate提供了一个ManagerCommand类，可以附加在flask-script的Manager类实例上
manager.add_command('db', MigrateCommand)

# flask的启动方法
if __name__ == '__main__':
    manager.run()
