from . import trainer, utils
from .trainer import EditFlowTrainer

# Lazy imports to avoid circular dependencies
def get_dream_models():
    from .models.dream.modelling_dream import (
        EditFlowDreamConfig,
        EditFlowDreamModel,
    )
    return EditFlowDreamConfig, EditFlowDreamModel

def get_llada_models():
    from .models.llada.modelling_llada import (
        EditFlowLLaDAConfig,
        EditFlowLLaDAModel,
    )
    return EditFlowLLaDAConfig, EditFlowLLaDAModel

def get_bert_models():
    from .models.bert.modelling_modernbert import (
        EditFlowModernBertConfig,
        EditFlowModernBertModel,
    )
    return EditFlowModernBertConfig, EditFlowModernBertModel
