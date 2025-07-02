from redis import Redis

# Redis client to subscribe to alert messages
redis_client = Redis(host='redis', port=6379, decode_responses=True)

# Subscribe to the 'alerts' channel where ingestor publishes alerts
pubsub = redis_client.pubsub()
pubsub.subscribe("alerts")

print("🚨 Alert Service Running...")

# Listen indefinitely for alert messages and print them
for msg in pubsub.listen():
    if msg['type'] == 'message':
        print(f"⚠️  ALERT: {msg['data']}")
