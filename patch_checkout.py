path = "/home/ubuntu/saleor-storefront/src/checkout/graphql/checkout.graphql"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """mutation checkoutLineDelete($checkoutId: ID!, $lineId: ID, $languageCode: LanguageCodeEnum!) {
	checkoutLineDelete(id: $checkoutId, lineId: $lineId) {"""

replacement = """mutation checkoutLineDelete($checkoutId: ID!, $lineId: ID!, $languageCode: LanguageCodeEnum!) {
	checkoutLineDelete: checkoutLinesDelete(id: $checkoutId, linesIds: [$lineId]) {"""

if target in content:
    content = content.replace(target, replacement)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: checkoutLineDelete patched to checkoutLinesDelete!")
else:
    print("Target not found, inspecting...")
