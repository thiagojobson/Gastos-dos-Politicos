from gastos_politicos.app import shell_context
from gastos_politicos.models import db, Politico, Reembolso, Feedback


def test_shell_context():
    """Testa o contexto do flask shell."""
    assert shell_context() == {
        "db": db,
        "Politico": Politico,
        "Reembolso": Reembolso,
        "Feedback": Feedback,
    }
