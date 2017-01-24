class TagBase(object):
    def __init__(self, element_name):
        self.element_name = element_name
        self.depth = 0
        self.tags = TagList()
        self.attributes = AttributeList()

    def add(self, content):
        try:
            if content.invalid:
                return
        except:
            pass
        if isinstance(content, AttributeBase):
            self.attributes.add(content)
        elif isinstance(content, AttributeList):
            self.attributes = content
        elif isinstance(content, TagBase):
            content.set_depth(self.depth+1)
            self.tags.add(content)
        elif isinstance(content, TagList):
            content.set_depth(self.depth+1)
            self.tags = content

    def set_name(self, name):
        name_attribute = Name(name)
        self.add(name_attribute)

    def set_depth(self, depth):
        self.depth = depth
        self.tags.set_depth(self.depth+1)

    @property
    def indentation(self):
        return self.depth*'    '

    @property
    def open_tag(self):
        return self.indentation \
               + '<' + self.element_name \
               + self.attributes.__str__() + '>'

    @property
    def close_tag(self):
        return self.indentation + '</'+self.element_name+'>'+'\n'

    def __str__(self):
        if self.attributes.empty and self.tags.empty:
            return ''
        return self.open_tag + '\n' + self.tags.__str__() + self.close_tag




class TagSimple(TagBase):
    
    def __init__(self, element_name, value):
        super().__init__(element_name)
        self.value = value

    @property
    def close_tag(self):
        return '</'+self.element_name+'>'+'\n'

    @property
    def convert_value(self):
        if hasattr(self.value, '__iter__') and not isinstance(self.value, str):
            return ' '.join(map(str, self.value))
        return str(self.value)
    
    def __str__(self):
        return self.open_tag + self.convert_value + self.close_tag




class TagList(object):
    def __init__(self, lst=[]):
        self.contents = lst[:]

    @property
    def empty(self):
        return (len(self.contents) == 0)

    def add(self, tag):
        self.contents.append(tag)

    def set_depth(self, depth):
        for tag in self.contents:
            tag.set_depth(depth)

    def __str__(self):
        data = ''
        for tag in self.contents:
            data += tag.__str__()
        return data


class AttributeList(object):
    def __init__(self, lst=[]):
        self.contents = lst[:]

    def add(self, attribute):
        self.contents.append(attribute)

    @property
    def empty(self):
        return (len(self.contents) == 0)

    def __str__(self):
        data = ''
        for attribute in self.contents:
            data += attribute.__str__()
        return data


class AttributeBase(object):
    def __init__(self, element_name, value=''):
        self.element_name = element_name
        self.value = value

    @property
    def invalid(self):
        return (self.value==None)

    @property
    def convert_value(self):
        if hasattr(self.value, '__iter__') and not isinstance(self.value, str):
            return ' '.join(map(str, self.value))
        return str(self.value)

    def __str__(self):
        return ' '+ self.element_name + '="' \
                  + self.convert_value + '"'
