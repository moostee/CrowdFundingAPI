from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                if field_name == 'isDeleted': pass
                self.fields.pop(field_name)
    
    def to_representation(self, instance):
        """Convert `name` to lowercase."""
        ret = super().to_representation(instance)
        if "name" in ret.keys(): ret['name'] = ret['name'].lower()
        return ret
