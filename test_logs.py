from log_chain import TamperEvidentLog

log_system = TamperEvidentLog()

log_system.add_log("LOGIN", "User login")
log_system.add_log("TRANSFER", "₹1000 sent")

# Tampering
log_system.chain[1].description = "HACKED DATA"

print(log_system.verify_logs())