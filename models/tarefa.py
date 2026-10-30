from datetime import datetime
from tarefas.models.database import Database


class Tarefa:
    """
    Provê métodos para armazenar, recuperar e processar os dados
    das tarefas criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva uma tarefa no banco de dados."""

        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)

        # Conexão padrão sem usar o 'with'
        db = Database()
        if db.conectar():
            db.executar(sql, params)
            db.desconectar()


# Area 51 (testes)
if __name__ == "__main__":
    tarefa = Tarefa('Minha nova tarefa')
    tarefa.salvarTarefa()