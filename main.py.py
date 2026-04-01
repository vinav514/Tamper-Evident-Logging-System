from log_chain import TamperEvidentLog
from utils import save_logs

log_system = TamperEvidentLog()

# Add logs
log_system.add_log("LOGIN", "User logged in")
log_system.add_log("TRANSACTION", "Sent ₹500")
log_system.add_log("LOGOUT", "User logged out")

# Verify logs
result = log_system.verify_logs()
print(result)

# Save logs
save_logs(log_system.chain)