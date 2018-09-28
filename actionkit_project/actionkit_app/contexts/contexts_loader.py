import account_contexts
import event_contexts
import base_contexts
import survey_contexts
import petition_contexts
import letter_contexts

contexts = {}

contexts.update({'accounts': account_contexts.contexts})
contexts.update({'events': event_contexts.contexts})
contexts.update({'base': base_contexts.contexts})
contexts.update({'survey': survey_contexts.contexts})
contexts.update({'petition': petition_contexts.contexts})
contexts.update({'letter': letter_contexts.contexts})
