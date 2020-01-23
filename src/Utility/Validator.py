import datetime
import re

class Validator:    
    def __init__(self, data={}, config=[]):
        self.ruleKeys = [field['field'] for field in config]
        missingValues = {key:None for key in self.ruleKeys if key not in data.keys()}
        data.update(missingValues)
        self.data = data
        self.config = config
        self.errors = {}
        self.isValid = True

    def minDate(self,field,ruleValue):
        try:
            self.type(field,'date')
            if ruleValue == 'today': ruleValue = datetime.date.today()
            if not isinstance(self.data[field], datetime.date):
                y,m,d = self.data[field].split('-')
                fieldData = datetime.date(int(y),int(m),int(d))
            if fieldData < ruleValue:
                self.__add_error(field,r"at least %s"%ruleValue)
        except BaseException as ex:
            return self
        return self

    def required(self,field,ruleValue):
        if ruleValue:
            if not self.data[field]: self.__add_error(field,"not be empty")
        return self
    
    def minLength(self,field,ruleValue):
        try:
            if len(self.data[field]) < ruleValue: self.__add_error(field,"at least {} characters.".format(ruleValue))
        except Exception:
            return self
        return self
    
    def maxLength(self,field,ruleValue):
        try:
            if len(self.data[field]) > ruleValue: self.__add_error(field,"at most {} characters.".format(ruleValue))
        except Exception:
            return self
        return self
    
    def minValue(self,field,ruleValue):
        try: 
            if self.data[field] < ruleValue: self.__add_error(field,r"at least %s"%ruleValue)
        except Exception:
            return self
        return self

    def type(self,field,ruleValue):
        if ruleValue == 'string':
            if not isinstance(self.data[field], str): self.__add_error(field,"be a string")
        elif ruleValue == 'boolean':
            if not isinstance(self.data[field], bool): self.__add_error(field,"be a boolean")
        elif ruleValue == 'number':
            try: float(self.data[field])
            except Exception: self.__add_error(field,'be a number')
        elif ruleValue == 'date':
            try:
                if not isinstance(self.data[field],datetime.date):
                    y,m,d = self.data[field].split('-')
                    datetime.datetime(int(y),int(m),int(d))
            except Exception:
                self.__add_error(field,'be a date (yyyy-mm-dd)')
        elif ruleValue == 'uuid':
            try:
                uuidPattern = '^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
                if not re.match(uuidPattern,self.data[field]): self.__add_error(field,"be uuid")
            except Exception:
                self.__add_error(field,"be uuid")
        return self
    
    def regex(self,field,ruleValue):
        try:
            if not re.match(ruleValue,self.data[field]): self.__add_error(field,r"of pattern: %s"%ruleValue)
        except Exception:
            self.__add_error(field,r"be of pattern: %s"%ruleValue)
        finally:
            return self

    def __add_error(self,field,type):
        self.isValid = False
        error = r"This field must {}".format(type)
        if field in self.errors.keys():
            self.errors[field].append(error)
            return self
        else:  
            self.errors[field] = [error]
            return self
    
    def __call_validator(self,rule,field,value):
        if rule == "required": self.required(field,value)
        elif rule == "minLength": self.minLength(field,value)
        elif rule == "maxLength": self.maxLength(field,value)
        elif rule == "minValue": self.minValue(field,value)
        elif rule == "minDate": self.minDate(field,value)
        elif rule == "type": self.type(field,value)
        elif rule == "regex": self.regex(field,value)
        return self
    
    def validate(self):
        for field in self.config:
            innerField = field['field']
            rules = field['rules']
            for rule in rules:
                key = rule['key']
                value = rule['value']
                self.__call_validator(key,innerField,value)
        return self
