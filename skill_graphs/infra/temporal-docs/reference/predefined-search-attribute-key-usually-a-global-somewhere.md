# Predefined search attribute key, usually a global somewhere
MY_KEYWORD_KEY = Temporalio::SearchAttributes::Key.new(
  'my-keyword',
  Temporalio::SearchAttributes::IndexedValueType::KEYWORD
)
