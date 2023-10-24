name='玛丽亚'
name='楚留冰'
print(name)#指向新的空间


name='玛丽亚'
name='楚留冰'
print(name)#可多次赋值，但会指向新的空间


name='玛丽亚'#原指向空间无人使用，就变成了系统垃圾
name='楚留冰'
print(name)

