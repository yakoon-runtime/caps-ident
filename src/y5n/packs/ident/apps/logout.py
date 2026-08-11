from y5n.sdk import io, ports


async def main():
    current = await ports.get("session").current()
    user = current.get("user_name") or ""

    auth = ports.get("ident.auth")
    await auth.logout()

    doc = ports.get("document")
    projection = await doc.render(name="default", state={"user": user})
    await io.write(projection)
