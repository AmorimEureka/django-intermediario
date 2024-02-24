from django.db import models
from stdimage.models import StdImageField

# Signals - É como se fosse uma trigger BEFORE/AFTER em Db's
from django.db.models import signals

# Recurso para acrescentar à url da página carregada
from django.template.defaultfilters import slugify

class Base(models.Model):
    """ Classe Abstrata, isto é, uma classe que não será uma entidade em db
        uma classe que possuí os campos em comum das demais classes criadas
        """
    criado = models.DateField('Data Criação', auto_now_add=True)
    modificado = models.DateField('Data Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Qtde Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb':(124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

# Antes de salvar na tabela executa a função acima
# Sempre que 'sender=Produto' submeter um sinal
signals.pre_save.connect(produto_pre_save, sender=Produto)