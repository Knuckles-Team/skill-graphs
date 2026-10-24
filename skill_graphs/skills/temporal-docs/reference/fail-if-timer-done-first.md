# Fail if timer done first
raise Temporalio::Error::ApplicationError, 'Timer expired' if sleep_fut.done?
