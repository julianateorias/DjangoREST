from rest_framework import serializers
from snippets.models import Snippet



class SnippetSerializer(serializers.ModelSerializer):
    """
    triple double quoted (docstring)
    A primeira parte da classe serializer define os campos que ficam serializados/deserializados.
    Metodos create() e update() define como instancias sao criadas ou modificadas quando chamado serializer.save()
    A classe serializer eh similar a classe Form do Django, incluindo silimares flags de validacao nos campos,
    como required, max_length e default.
    As field flags podem controlar como o serializer deve ser exibido em certas circunstancias, assim quando renderizado
    para o HTML.
    A flag {'base_template': 'textarea.html'} eh equivalente ao uso do widget=widgets.Textarea na classe Django Form.
    Eh um uso particular util para controlar como a navegavel API deve ser exibida.
    Tambem podemos salvar na classe ModelSerializer, sera visto mais tarde.

    Além das flags acima. tem a flag que usamos bastante many=True (quando recuperamos vários snippets do modelo,
    passamos essa flag para o serializer entender que vai criar ou atualizar mais de um).
    Uma instância SnippetSerializer recebe (data=data), e tem funções, como:
    serializer.is_valid()
    serializer.validated_data
    serializer.save()
    serializer.data
    serializer.errors
    """
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')



# A CLASSE ACIMA FAZ A MESMA COISA, POREM HERDANDO DE MODELSERIALIZER E USANDO NOSSO MODELO SNIPPET.
'''
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Cria e retorna uma nova instancia 'Snippet', dado os dados validos.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Atualiza e retorna uma instancia 'Snippet' existente, dado os dados validos.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
'''