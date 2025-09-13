from django.db import models
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    perfil = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    data_admissao = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class CategoriaEPI(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    categoria = models.ForeignKey(CategoriaEPI, on_delete=models.CASCADE, related_name="equipamentos")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, unique=True)
    numero_ca = models.CharField(max_length=50, blank=True, null=True)
    data_fabricacao = models.DateField(blank=True, null=True)
    data_validade = models.DateField(blank=True, null=True)
    tamanho = models.CharField(max_length=20, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.numero_serie})"


class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="emprestimos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField()
    data_previsao_devolucao = models.DateField(blank=True, null=True)
    data_devolucao_real = models.DateField(blank=True, null=True)
    observacoes_emprestimo = models.TextField(blank=True, null=True)
    observacoes_devolucao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)


class ItemEmprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, related_name="itens")
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True, null=True)
    status_item = models.CharField(max_length=50)


class HistoricoEquipamento(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name="historicos")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="historicos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="historicos")
    acao = models.CharField(max_length=100)
    data_acao = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    status_anterior = models.CharField(max_length=50, blank=True, null=True)
    status_novo = models.CharField(max_length=50, blank=True, null=True)
# Create your models here.
