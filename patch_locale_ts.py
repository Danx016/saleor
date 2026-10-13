path = "/home/ubuntu/saleor-storefront/src/config/locale.ts"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# Add es to LOCALE_DEFINITIONS
if "es:" not in c:
    c = c.replace(
        "export const LOCALE_DEFINITIONS = {",
        """export const LOCALE_DEFINITIONS = {
	es: {
		bcp47: "es-CO",
		graphqlLanguageCode: "ES",
		htmlLang: "es",
		ogLocale: "es_CO",
	},"""
    )

# Change default from en to es
c = c.replace('return "en";', 'return "es";')

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("LOCALE_DEFINITIONS patched with Spanish as default!")
