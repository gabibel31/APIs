def clean_clients(clients):
    cleaned = []
    seen_emails = set()

    stats = {
        "removed_empty_email":0,
        "removed_duplicates":0,
        "removed_invalid_name":0,
    }

    for client in clients:
        if not client.bame or not client.name.strip():
            stats["removed_invalid_name"] += 1
            continue
        if not client.email:
            stats["removed_empty_email"] += 1
            continue
        seen_emails.add(client.email)
        cleaned.append(client)

    return {
        "cleaned_clients": cleaned,
        "stats": stats
    }