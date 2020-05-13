<template>
  <div id="two">
    index  count  replace split startswith  endswith upper lower isalpha isdigit title isalnum
    <br>

    列表中最大值：
    <br>
    max(list)
    <br>

    python中的内置函数：
    <br>
    max()
    min()
    del()
    len()
    sum()
    用于任何数据类型
    
    原样输出：print 
    <br>
    单行注释：
    <br>
    #注释内容     快捷键： ctrl+/
    <br>
    多行注释：
    <br>
    """注释内容"""   也可以用单引号   '''注释内容'''
    <br>
    print(type(a))输出a的类型
    <br>
    输入函数
    <br>
    a=input("提示内容")  赋给a值  是字符串  用强制转换将a变成其他类型 如：int(a) 变成整型
    <br>
    %d 整型
    <br>
    %f  浮点型
    <br>
    %s 字符串型
    <br>
    %c 字符型
    <br>
    a=[3,1,2,5,4]
    <br>
    a.sort(reverse=True)
    <br>
    print(a)  倒序
    <br>

    字符串：str
    <br>
    数字类型：整型 int 浮点型 float
    <br>
    布尔类型：1=true 0=false
    <br>
    列表：list  =[1,2,3]
    <br>
    元祖：tuple= (1,2)
    <br>
    字典：dict ={"name":"123","age":18}
    <br>
    集合：set = {1,2,3,4}
    <br>
    <br>
    if 条件一:
    <br>
      print()
      <br>
    elif 条件二：
    <br>
      print()
      <br>
    else :
    <br>
      print()
      <br>

    name="abcdef"
    <br>
    输出下标为0  print(name[0])
    <br>

    切片： 范围是左闭右开！！！
    <br>
    print(name[0:3])    结果：abc
    <br>
    print(name[0:5:2]  结果：ace
    <br>
    print(name[0:-1:2]  结果：ace
    <br>
    print(name[5:0:-2] 结果：fdb
    <br>
    print(name[5:0:-1] 结果:fedcb
    <br>
    print(name[:3] 结果：abc
    <br>

    字符串的常见操作：
    <br>
    my="hello world hello python"
    <br>
    1、find():检测字符串里是否包含你要查询的字符串
    <br>
    例如：
    <br>
    print(my.find("python"))
    <br>
    如果存在返回开始的索引值（也就是下标）
    <br>
    不存在返回值为-1
    <br>
    2、index():检测你设定的字符串长度里是否存在你要查询的字符串
    <br>
    例如：
    <br>
    print(my.index("py",0,25))
    <br>
    如果存在返回开始的索引值，否则报错，index里的第一个数字参数是起始，后一个是终止的索引值-1
    <br>

    3、count:查询出现的次数
    <br>
    a=len("123")  a的值为该字符串的长度 a=3
    <br>
    print(my.count("l"))
    <br>
    结果为5
    <br>
    my_str.count(str, 0, len(mystr))
    <br>

    4、replace() 替换
    <br>
    my_str.replace("l","r",2)  将l替换为r 两次
    <br>

    5、split() 切片
    <br>
    以str为分隔符切片mystr,如果maxsplit有指定值，则仅分割maxsplit个字符串
    <br>
    格式：my_str.split(str=" ",2)
    <br>
    my_str.split(" ")  以空格为切片条件
    <br>
    结果为：['hello','world','hello','python']为列表结构
    <br>
    str="qaqwrwrwee"
    <br>
    print(str.split("w",2))
    <br>
    结果为：['qaq','r','rwee'] 2表示切两次  以w为切点  结果没有切点
    <br>

    6、startswith()
    <br>
    检查字符串是否以( )开头 是返回True 不是返回False
    <br>
    my_str.startswith("hello") 结果为：True 
    <br>

    7、endswith() 查询是否以什么什么结尾
    <br>

    4、upper()：转换my中的小写字母为大写
    <br>
    print(my.upper())
    <br>

    5、lower():转换my中的大写字符为小写
    <br>
    print(my.lower())
    <br>

    6、title():把字符串的每个单词首字母大写
    <br>
    print(my.title())
    <br>

    7、capitalize():把字符串的第一个字符大写
    <br>
    print(my.capitalize())
    <br>

    8、splitlines():按照行分隔，返回一个包含各行作为元素的列表
    <br>
    例如：
    <br>
    my_name="hello\nworld"
    <br>
    print(my_name) 
    <br>
    结果为：
    <br>
    hello
    <br>
    world
    <br>
    print(my_name.spiltlines())
    <br>
    结果为：
    <br>
    ["hello","world"]
    <br>

    9、isalpha():如果my所有字符都是字母 则返回True,否则返回False
    <br>
    print(my.isalpha())
    <br>
    结果为：True
    <br>

    10、isdigit()：如果my只包含数字则返回True 否则返回False
    <br>
    print(my.isdigit())
    <br>
    结果为：False
    <br>

    11、isalnum():如果my所有字符都是字母或数字则返回True,否则返回False
    <br>
    print(my.isalnum())
    <br>
    结果为True
    <br>

    12、isspace():如果my中只包含空格，则返回True,否则返回False
    <br>
    print(my.isspace())
    <br>
    结果为：False
    <br>

    13、rfind()
    <br>
    从右往左找你要查找的字符串  找到后返回下标值
    <br>
    a=rfind('.')  用来取文件的后缀名
    <br>

    14、join
    <br>
    用来将列表里的元素连接变为字符串
    <br>
    一行代码实现九九乘法表
    <br>
    print('.'.join([1,2]))
    <br>
    结果为'1.2'
    <br>


    列表：
    <br>
    增加（append,extend,insert）
    <br>
    append:
    <br>
    A=[1,2,3]
    <br>
    A.append("4")
    <br>
    结果为：A=[1,2,3,"4"]
    <br>

    extend:
    <br>
    a=[1,2]  b=[3,4]
    <br>
    a.extend(b)
    <br>
    结果为 a=[1,2,3,4]
    <br>
    a.append(b)
    <br>
    结果为 a=[1,2,[3,4]]
    <br>

    insert:
    <br>
    a=[0,1,2]
    <br>
    a.insert(1,3)
    <br>
    结果为 a=[0,3,1,2]
    <br>

    修改元素：
    <br>
    a=[1,2,3]
    <br>
    a[0]=3
    <br>
    结果为：a=[3,2,3]
    <br>

    查找元素：
    <br>
    1、in判断存在
    <br>
    name="123456789"
    <br>
    find="123"
    <br>
    if find in name:
    <br>
      print("存在")
      <br>
    else:
    <br>
      print("不存在")
      <br>
    2、not in判断不存在
    <br>

    3、index和count和在字符串里的应用一样
    <br>

    删除元素：
    <br>
    list=[1,2,3]
    <br>
    1、del list[1]
    <br>
    2、list.pop()删除最后一个元素
    <br>
    3、list.remove(1)
    <br>


<br>
    排序
    <br>
    list.sort()  从小到大排序
    <br>
    list.sort(reverse=Ture)从大到小排序
    <br>
    list.reverse()反转
    <br>

    列表的嵌套
    <br>
    list=[1,[2,3],4]
    <br>
    list[1].insert(1,5)结果为list[1,[2,5,3],4]
    <br>
<br>

    字典：
    <br>
    字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
    <br>
    info={"name":'师玲珑',"age":18}
    <br>
    print(info["name"])  结果为：师玲珑
    <br>

    修改数据：
    <br>
    info["age"]=20
    <br>

    删除数据
    <br>
    del info["age"]
    <br>

    info.clear()删除所有数据
    <br>

    如果info中不存在'age'这个键，我就让他返回默认值18
    <br>
    age=info.get('age',18)
    <br>
    print(age)
    <br>

    len()测量字典中，键值对的个数
    <br>
    print(info.keys()) 返回一个包含字典所有的key列表  
    <br>
    结果为：info_keys(['name','age','sex'])
    <br>

    print(info.values()) 返回一个包含字典所有的value列表  
    <br>
    结果为：info_values([18,20,'女'])
    <br>

    print(info.items()) 返回一个包含字典所有的键值对列表  
    <br>
    结果为：info_values([('name','age','sex'),(18,20,'女')])
    <br>

    遍历字典的key   210 480  690
    <br>
    for key in info.keys():
    <br>
          print(key)
          <br>

    遍历字典的values
    <br>
    for value in info.values():
    <br>
        print(value)                    
        <br>

    遍历字典的items
    <br>
    for item in info.items():
    <br>
        print(item)
        <br>
    或者
    <br>
    for key,value in info.items()
    <br>
        print(key,value)
        <br>

    如何实现带下标的遍历
    <br>
    chars=[1,2,3,4]
    <br>
    for i,chr in enumerate(chars):
    <br>
        print(i,chr)
        <br>
    结果为：
    <br>
    0 1
    <br>
    1 2 
    <br>
    2 3 
    <br>
    3 4
    <br>

    ——————————————————————————----——————————————————————————————————————————————
    集合：
    <br>
    集合是无序的，集合中的元素是唯一的，集合一般用于元组或者列表中的元素去重。
    <br>

    添加元素
    <br>
    add:
    <br>
    set1={1,2,3}
    <br>
    set1.add(8) 
    <br>
    print(set1)
    <br>
    结果为 1,2,3,8
    <br>

    update:
    <br>
    set1={1,2,3}
    <br>
    set1.update("abcd")
    <br>
    print(set1)
    <br>
    结果为：1,2,3,a,b,c,d
    <br>

    删除元素
    <br>
    set1.remove(1)如果没有报错
    <br>

    set1.discard(1) 如果没有不执行
    <br>

    set1.pop()是随机删除集合中的元素
    <br>

    交集：
    <br>
    set1={1,2,3}
    <br>
    set2={3,4}
    <br>
    new_set=set1&set2
    <br>
    print(new_set) 结果为{3}
    <br>

    并集：
    <br>
    new_set=set1|set2 
    <br>
    print(new_set) 结果为{1,2,3,4}
    <br>

    ——————————————————————————----——————————————————————————————————————————————
    <br>
    公共方法：
    <br>
    运算符     python表达式      结果           描述                    支持的数据类型
    <br>
    +              [1,2]+[3,4]       [1,2,3,4]         合并                    字符串.列表.元祖      
    <br>
    *               [1]*4               [1,1,1,1]          复制	                   字符串.列表.元祖
    <br>
    in             3 in (1,2,3)          True         元素是否存在         同上+字典
    <br>
    not in     4 not in(1,2,3)        True         元素是否不存在     同上
    <br>








  </div>
</template>
<script>
import Qs from 'qs'
import Router from '@/router/index'
export default {
  name:'#two',
  data(){
    return{
    }
  },
  methods:{
   }
}
</script>