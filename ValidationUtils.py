class ValidationUtils:

    @staticmethod
    def isNone(obj, errorMessage, errorType):
        if obj is None:
            raise errorType(errorMessage)

    @staticmethod
    def mustBeTrue(condition, errorMessage, errorType):
        if not condition:
            raise errorType(errorMessage)

    @staticmethod
    def isSubclassOf(obj, subclass_tuple, errorMessage):
        if not issubclass(obj, subclass_tuple):
            raise TypeError(errorMessage)

    @staticmethod
    def isInstanceOf(obj, objectType_tuple, errorMessage):
        if not isinstance(obj, objectType_tuple):
            raise TypeError(errorMessage)
