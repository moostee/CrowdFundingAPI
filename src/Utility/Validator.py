import datetime
import re

class Validator:
    def __init__(self, data, rules):
        missingValues = {key:None for key in rules.keys() if key not in data.keys()}
        data.update(missingValues)
        self.data = data
        self.rules = rules
        self.errors = {}
        self.isValid = True
    
    def string(self,field,value):
        if not isinstance(value, str): self.__add_error(field,"a string")
        return self
    
    def bool(self,field,value):
        if not isinstance(value, bool): self.__add_error(field,"a boolean")
        return self
    
    def number(self,field,value):
        try:
            float(value)
        except Exception:
            self.__add_error(field,'a number')
        finally:
            return self
    
    def date(self,field,value):
        try:
            y,m,d = value.split('-')
            datetime.datetime(int(y),int(m),int(d))
        except Exception:
            self.__add_error(field,'a date (yyyy-mm-dd)')
            return self
        finally:
            return self
    
    def pattern(self,field,value,rule):
        try:
            pattern = rule.split(':')[1]
            if not re.match(pattern,value): self.__add_error(field,r"of pattern: %s"%pattern)
        except Exception:
            self.__add_error(field,r"of pattern: %s"%pattern)
        finally:
            return self
    
    def after(self,field,value,rule):
        self.date(field,value)
        dateString = rule.split(':')[1]
        if value < dateString: self.__add_error(field,r"after %s"%dateString)
        return self

    def enum(self,field,value,rule):
        enumz = rule.split(':')[1].split(',')
        if value not in enumz: self.__add_error(field,'one of: '+str(enumz))
        return self

    def uuid(self,field,value):
        try:
            pattern = '^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
            if not re.match(pattern,value): self.__add_error(field,"uuid")
        except Exception:
            self.__add_error(field,"uuid")
        finally:
            return self

    def __add_error(self,field,type):
        self.isValid = False
        error = r"This field must be {}".format(type)
        if field in self.errors.keys():
            self.errors[field].append(error)
            return self
        else:  
            self.errors[field] = [error]
            return self
    
    def __call_validator(self,rule,field,value):
        if rule == "string": self.string(field,value)
        elif rule == "bool": self.bool(field,value)
        elif rule == "number": self.number(field,value)
        elif rule == "date": self.date(field,value)
        elif rule == 'uuid': self.uuid(field,value)
        elif rule.startswith('pattern'): self.pattern(field,value,rule)
        elif rule.startswith('enum'): self.enum(field,value,rule)
        elif rule.startswith('after'): self.after(field,value,rule)
        return self


    def validate(self):
        for i in self.rules:
            if '|' in self.rules[i] and not self.rules[i].startswith('pattern'):
                for param in self.rules[i].split('|'):
                    self.__call_validator(param,i,self.data[i])
            else:
                self.__call_validator(self.rules[i],i,self.data[i])
        return self
