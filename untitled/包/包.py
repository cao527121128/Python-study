#coding=utf-8
'''
思考：如果不同的人编写的模块名同名如何解决？
解决：为了解决模块名重名的冲突，引入了按目录结构来组织模块的方法，称为包

特点：引入包以后，还要顶层目录与其他的不一样，就可以保证该模块不会与其他模块命名发生冲突

注意：目录中只有包含一个叫做"__init__.py"的文件才可以被认为是一个包，基本上目前这个文件不需要写任何内容


'''
# 示例1
#import a.Linuxcao
#import b.Linuxcao

#a.Linuxcao.sayGood()
#b.Linuxcao.sayGood()

# 示例2  模块简称
import a.Linuxcao as aLinuxcao
import b.Linuxcao as bLinuxcao

aLinuxcao.sayGood()
bLinuxcao.sayGood()

