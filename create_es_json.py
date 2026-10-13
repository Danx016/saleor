import json

with open("c:/Users/danil/Downloads/saleor-main/saleor-main/en.json", "r", encoding="utf-8") as f:
    en = json.load(f)

# Complete professional Spanish translation dictionary for Saleor Storefront
es = {
    "cart": {
        "drawer": {
            "itemCount": "{count, plural, one {# producto} other {# productos}}",
            "subtotal": "Subtotal",
            "shipping": "Envío",
            "shippingFree": "Gratis",
            "shippingCalculated": "Calculado en la pantalla de pago",
            "total": "Total",
            "checkout": "Finalizar compra",
            "continueShopping": "Seguir comprando",
            "removeItem": "Eliminar {product}",
            "decreaseQuantity": "Disminuir cantidad",
            "increaseQuantity": "Aumentar cantidad"
        },
        "page": {
            "title": "Carrito de compras",
            "quantity": "Cant: {count}",
            "variant": "Variante: {name}",
            "yourTotal": "Tu total",
            "shippingNote": "El envío se calculará en el siguiente paso",
            "checkout": "Finalizar compra"
        }
    },
    "productsListing": {
        "breadcrumbHome": "Inicio",
        "breadcrumbProducts": "Productos"
    },
    "common": {
        "pagination": {
            "previous": "Anterior",
            "next": "Siguiente"
        }
    },
    "pdp": {
        "addToBag": "Añadir al carrito",
        "adding": "Añadiendo…",
        "outOfStock": "Agotado",
        "selectOptions": "Seleccionar opciones",
        "buyBox": {
            "overBudgetHint": "Este producto tiene demasiadas opciones. Abre un enlace de variante específico para comprar.",
            "externalHint": "Las opciones de este producto se seleccionan en una experiencia personalizada.",
            "selectedSummary": "Opciones seleccionadas"
        },
        "free": "GRATIS",
        "breadcrumbHome": "Inicio",
        "badges": {
            "sale": "Oferta",
            "new": "Nuevo",
            "bestseller": "Más vendido"
        },
        "variant": {
            "outOfStockTitle": "{name} - Agotado",
            "willChangeSelections": "{name} - Cambiará otras selecciones",
            "percentOffTitle": "{name} - {percent}% de descuento",
            "outOfStockA11y": "agotado",
            "percentOffA11y": "{percent}% de descuento",
            "selectedA11y": "seleccionado",
            "chooseOption": "Elegir {label}",
            "searchOptions": "Buscar {label}",
            "noMatchingOptions": "No hay opciones coincidentes"
        },
        "attributes": {
            "description": "Descripción",
            "productDetails": "Detalles del producto",
            "careInstructions": "Instrucciones de cuidado",
            "shippingReturns": "Envíos y devoluciones",
            "shippingBody": "Envío gratis en pedidos superiores a {freeShippingThreshold}. Entrega estándar de 3 a 5 días hábiles.",
            "returnsBody": "Devoluciones gratuitas dentro de los {returnsWindowDays} días posteriores a la compra.",
            "yes": "Sí",
            "no": "No"
        },
        "zoom": {
            "title": "{productName} — imagen ampliada",
            "imageAlt": "{productName} — vista {index}",
            "close": "Cerrar imagen ampliada",
            "previous": "Imagen anterior",
            "next": "Imagen siguiente",
            "counter": "{current} / {total}"
        }
    },
    "plp": {
        "quickAdd": "Añadir rápido",
        "filtersButton": "Filtros",
        "filterLabels": {
            "category": "Categoría",
            "color": "Color",
            "size": "Tamaño",
            "price": "Precio",
            "priceRange": "Rango de precio"
        },
        "sort": "Ordenar",
        "sortOptions": {
            "featured": "Destacados",
            "newest": "Más recientes",
            "price_asc": "Precio: Menor a mayor",
            "price_desc": "Precio: Mayor a menor",
            "bestselling": "Más vendidos"
        },
        "resultCount": "{count, plural, one {# producto} other {# productos}}",
        "clearAllFilters": "Limpiar todos los filtros ({count})",
        "clearAll": "Limpiar todo",
        "removeFilter": "Eliminar filtro {value}",
        "noMatchingFilters": "No hay productos que coincidan con tus filtros."
    },
    "search": {
        "title": "Buscar",
        "description": "Busca en todo nuestro catálogo de productos.",
        "bar": {
            "placeholder": "Buscar productos…",
            "srOnlyLabel": "Buscar productos"
        },
        "resultsFor": "Resultados para \"{query}\"",
        "resultCount": "{count, plural, one {# producto encontrado} other {# productos encontrados}}",
        "noResultsTitle": "Sin resultados para \"{query}\"",
        "noResultsBody": "No pudimos encontrar productos que coincidan con tu búsqueda. Intenta con otro término o explora las categorías.",
        "browseAllProducts": "Ver todos los productos",
        "goToHomepage": "Ir al inicio",
        "noImage": "Sin imagen",
        "sort": "Ordenar",
        "sortOptions": {
            "relevance": "Relevancia",
            "price-asc": "Precio: Menor a mayor",
            "price-desc": "Precio: Mayor a menor",
            "name": "Nombre",
            "newest": "Más recientes"
        }
    },
    "nav": {
        "header": {
            "mainAriaLabel": "Principal"
        },
        "breadcrumbAriaLabel": "Migas de pan",
        "cartButton": "{count, plural, one {# producto en el carrito, ver bolsa} other {# productos en el carrito, ver bolsa}}",
        "mobileMenu": {
            "open": "Abrir menú",
            "title": "Menú de navegación"
        },
        "userMenu": {
            "open": "Abrir menú de usuario",
            "login": "Iniciar sesión",
            "myAccount": "Mi cuenta",
            "myOrders": "Mis pedidos",
            "logOut": "Cerrar sesión",
            "unavailableAriaLabel": "Cuenta no disponible",
            "unavailableTitle": "No se pudo cargar la cuenta"
        },
        "regionPicker": {
            "ariaLabel": "Idioma y mercado",
            "languageTitle": "Idioma",
            "languageDescription": "Textos y formato del sitio",
            "marketTitle": "Mercado",
            "marketDescription": "Moneda, impuestos y envíos"
        }
    },
    "account": {
        "metadata": {
            "loginTitle": "Iniciar sesión",
            "loginDescription": "Inicia sesión en tu cuenta para acceder a tus pedidos y direcciones guardadas.",
            "signupTitle": "Crear cuenta",
            "signupDescription": "Crea una nueva cuenta para guardar tus direcciones e historial de pedidos.",
            "accountTitle": "Mi cuenta"
        },
        "fields": {
            "email": "Correo electrónico",
            "emailAddress": "Dirección de correo electrónico",
            "password": "Contraseña",
            "firstName": "Nombre",
            "lastName": "Apellido",
            "confirmPassword": "Confirmar contraseña",
            "currentPassword": "Contraseña actual",
            "newPassword": "Nueva contraseña",
            "confirmNewPassword": "Confirmar nueva contraseña",
            "name": "Nombre",
            "companyOptional": "Empresa (opcional)",
            "streetAddress": "Dirección",
            "streetAddress2Optional": "Apto, suite, unidad (opcional)",
            "city": "Ciudad",
            "postalCode": "Código postal",
            "stateProvince": "Departamento / Provincia",
            "countryCode": "Código de país",
            "phoneOptional": "Teléfono (opcional)",
            "country": "País",
            "cityArea": "Zona / Barrio",
            "localized": {
                "province": "Provincia",
                "district": "Distrito",
                "state": "Departamento / Estado",
                "zip": "Código postal",
                "postal": "Código postal",
                "postTown": "Municipio",
                "prefecture": "Prefectura"
            }
        },
        "placeholders": {
            "email": "tu@ejemplo.com",
            "password": "Ingresa tu contraseña",
            "firstName": "Nombre",
            "lastName": "Apellido",
            "newPasswordMin": "Al menos 8 caracteres…",
            "confirmPassword": "Confirma tu contraseña",
            "reenterPassword": "Vuelve a ingresar tu contraseña",
            "countryCode": "CO"
        },
        "common": {
            "cancel": "Cancelar",
            "save": "Guardar",
            "saving": "Guardando…",
            "edit": "Editar",
            "delete": "Eliminar",
            "updated": "Actualizado",
            "showPassword": "Mostrar contraseña",
            "hidePassword": "Ocultar contraseña",
            "free": "Gratis",
            "qty": "Cant: {count}",
            "itemCount": "{count, plural, one {# producto} other {# productos}}",
            "notSet": "No establecido",
            "change": "Cambiar",
            "changing": "Cambiando…",
            "sending": "Enviando…"
        },
        "errors": {
            "invalidEmail": "Por favor ingresa un correo electrónico válido",
            "invalidEmailFirst": "Primero ingresa un correo electrónico válido",
            "passwordRequired": "Por favor ingresa tu contraseña",
            "passwordMinLength": "La contraseña debe tener al menos 8 caracteres",
            "passwordsMismatch": "Las contraseñas no coinciden",
            "newPasswordRequired": "Por favor ingresa una nueva contraseña",
            "generic": "Ocurrió un error. Por favor inténtalo de nuevo.",
            "signInFailed": "Error al iniciar sesión. Inténtalo de nuevo.",
            "invalidCredentials": "Correo o contraseña incorrectos. Inténtalo de nuevo.",
            "rateLimited": "Demasiados intentos de inicio de sesión. Espera un momento.",
            "resetLinkFailed": "Error al enviar el enlace de recuperación",
            "accountExists": "Ya existe una cuenta con este correo. Por favor inicia sesión.",
            "createAccountFailed": "Error al crear la cuenta",
            "invalidResetToken": "Este enlace de restablecimiento ha expirado.",
            "setPasswordFailed": "Error al establecer la contraseña",
            "invalidConfirmToken": "Este enlace de confirmación ha expirado o ya fue utilizado.",
            "confirmFailed": "Error al confirmar la cuenta",
            "loadOrdersFailed": "No pudimos cargar tus pedidos. Inténtalo en un momento.",
            "loadOrderFailed": "No pudimos cargar este pedido. Inténtalo de nuevo.",
            "loadRecentOrdersFailed": "No pudimos cargar tus pedidos recientes.",
            "updateProfileFailed": "Error al actualizar el perfil",
            "changePasswordFailed": "Error al cambiar la contraseña",
            "createAddressFailed": "Error al guardar la dirección",
            "updateAddressFailed": "Error al actualizar la dirección",
            "deleteAddressFailed": "Error al eliminar la dirección",
            "setDefaultAddressFailed": "Error al establecer la dirección predeterminada",
            "deleteAccountFailed": "Error al solicitar la eliminación de la cuenta"
        },
        "login": {
            "title": "Bienvenido de nuevo",
            "noAccount": "¿No tienes una cuenta?",
            "signUp": "Regístrate",
            "forgotPassword": "¿Olvidaste tu contraseña?",
            "resendResetLink": "Reenviar enlace de recuperación",
            "submit": "Iniciar sesión",
            "submitting": "Iniciando sesión…",
            "resetSent": "Si existe una cuenta para {email}, hemos enviado un enlace de restablecimiento."
        },
        "signup": {
            "title": "Crear una cuenta",
            "hasAccount": "¿Ya tienes una cuenta?",
            "signIn": "Iniciar sesión",
            "submit": "Crear cuenta",
            "submitting": "Creando cuenta…",
            "successTitle": "¡Cuenta creada con éxito!",
            "successBody": "Por favor revisa tu correo electrónico para verificar tu cuenta.",
            "goToSignIn": "Ir a iniciar sesión",
            "terms": "Al crear una cuenta, aceptas nuestros <terms>Términos de servicio</terms> y <privacy>Política de privacidad</privacy>.",
            "termsLink": "Términos de servicio",
            "privacyLink": "Política de privacidad"
        },
        "setPassword": {
            "title": "Establecer nueva contraseña",
            "subtitle": "Ingresa una nueva contraseña para {email}",
            "submit": "Actualizar contraseña",
            "submitting": "Actualizando…",
            "backToSignIn": "Volver a iniciar sesión",
            "successTitle": "¡Contraseña actualizada!",
            "successBody": "Tu contraseña se ha restablecido exitosamente. Ahora has iniciado sesión.",
            "redirecting": "Redirigiéndote a la tienda…"
        },
        "confirm": {
            "successTitle": "Cuenta confirmada",
            "successBody": "Tu cuenta para {email} está activa.",
            "signIn": "Iniciar sesión",
            "continueShopping": "Seguir comprando",
            "errorTitle": "No se pudo confirmar la cuenta",
            "goToSignIn": "Ir a iniciar sesión",
            "title": "Confirma tu cuenta",
            "body": "Ingresa la contraseña para {email} para terminar de confirmar tu cuenta.",
            "submit": "Confirmar cuenta",
            "submitting": "Confirmando…",
            "tryAgain": "Intentar de nuevo"
        },
        "nav": {
            "ariaLabel": "Cuenta",
            "backToStore": "Volver a la tienda",
            "signOut": "Cerrar sesión",
            "overview": "Resumen",
            "orders": "Pedidos",
            "addresses": "Direcciones",
            "settings": "Configuración"
        },
        "overview": {
            "welcome": "Bienvenido, {name}",
            "subtitle": "Aquí tienes un resumen de la actividad de tu cuenta.",
            "recentOrders": "Pedidos recientes",
            "viewAll": "Ver todos",
            "noOrdersYet": "Aún no has realizado ningún pedido."
        },
        "orders": {
            "title": "Pedidos",
            "count": "{count, plural, =0 {Sin pedidos aún} one {# pedido} other {# pedidos}}",
            "empty": "Aún no has realizado ningún pedido.",
            "loadMore": "Cargar más pedidos",
            "signInRequired": "Inicia sesión para ver tus pedidos.",
            "orderNumber": "ORD-{number}"
        },
        "orderDetail": {
            "placedOn": "Realizado el {date}",
            "items": "Productos ({count})",
            "subtotal": "Subtotal",
            "shipping": "Envío",
            "tax": "Impuestos",
            "total": "Total",
            "shippingAddress": "Dirección de envío",
            "billingAddress": "Dirección de facturación",
            "paymentMethod": "Método de pago",
            "paid": "Pagado",
            "needHelp": "¿Necesitas ayuda?",
            "signInRequired": "Inicia sesión para ver este pedido.",
            "loadFailed": "No pudimos cargar este pedido. Inténtalo de nuevo.",
            "timeline": "Cronología del pedido"
        },
        "orderStatus": {
            "UNFULFILLED": "En preparación",
            "UNCONFIRMED": "Pendiente de confirmación",
            "PARTIALLY_FULFILLED": "Enviado parcialmente",
            "FULFILLED": "Enviado"
        },
        "fulfillment": {
            "orderConfirmed": "Pedido confirmado",
            "orderConfirmedDescription": "Pago confirmado y pedido registrado",
            "FULFILLED": "Enviado",
            "FULFILLEDDescription": "Tu pedido ha sido enviado",
            "CANCELED": "Envío cancelado",
            "CANCELEDDescription": "El envío fue cancelado",
            "REFUNDED": "Reembolsado",
            "REFUNDEDDescription": "El pago ha sido reembolsado",
            "REFUNDED_AND_RETURNED": "Reembolsado y devuelto",
            "REFUNDED_AND_RETURNEDDescription": "Productos devueltos y reembolsados",
            "REPLACED": "Reemplazado",
            "REPLACEDDescription": "Los productos han sido reemplazados",
            "RETURNED": "Devuelto",
            "RETURNEDDescription": "Los productos han sido devueltos",
            "WAITING_FOR_APPROVAL": "En espera de aprobación",
            "WAITING_FOR_APPROVALDescription": "El envío está pendiente de aprobación",
            "trackingUpdated": "Seguimiento actualizado",
            "trackingNumber": "Número de guía: {number}",
            "descriptionWithItems": "{description} ({count, plural, one {# producto} other {# productos}})"
        },
        "settings": {
            "title": "Configuración",
            "subtitle": "Administra la configuración de tu cuenta",
            "memberSince": "Miembro desde {date}"
        },
        "addresses": {
            "title": "Direcciones",
            "subtitle": "Administra tus direcciones guardadas",
            "empty": "No hay direcciones guardadas aún.",
            "addAddress": "Añadir dirección",
            "editAddress": "Editar dirección",
            "addNewAddress": "Añadir nueva dirección",
            "editAddressDescription": "Actualiza los datos de tu dirección",
            "addAddressDescription": "Añade una nueva dirección a tu cuenta",
            "editAddressAria": "Editar dirección",
            "updateAddress": "Actualizar dirección",
            "deleteAddressAria": "Eliminar dirección",
            "defaultShipping": "Envío predeterminado",
            "defaultBilling": "Facturación predeterminada",
            "makeDefaultShipping": "Establecer como envío predeterminado",
            "makeDefaultBilling": "Establecer como facturación predeterminada"
        },
        "deleteAccount": {
            "title": "Eliminar cuenta",
            "description": "Eliminar permanentemente tu cuenta y todos los datos asociados.",
            "submit": "Eliminar cuenta",
            "confirm": "Sí, eliminar mi cuenta",
            "confirmBody": "Esta acción no se puede deshacer.",
            "emailSent": "Se ha enviado un correo electrónico de confirmación."
        },
        "changePassword": {
            "submit": "Cambiar contraseña"
        },
        "unavailable": {
            "title": "No se puede cargar tu cuenta",
            "body": "La tienda no está disponible temporalmente. Actualiza la página o inténtalo en un momento."
        }
    },
    "checkout": {
        "steps": {
            "information": "Información",
            "shipping": "Envío",
            "payment": "Pago",
            "stepsAriaLabel": "Pasos de pago",
            "secureCheckout": "Pago seguro",
            "complete": "Completado",
            "stepOf": "Paso {step} de {total}"
        },
        "actions": {
            "saving": "Guardando…",
            "loading": "Cargando…",
            "continueToShipping": "Continuar al envío",
            "continueToPayment": "Continuar al pago",
            "continue": "Continuar",
            "continueAsGuest": "Continuar como invitado",
            "preparingGuestCart": "Preparando carrito de invitado…",
            "logIn": "Iniciar sesión",
            "returnToInformation": "Volver a información",
            "returnToShipping": "Volver a envío",
            "payNow": "Pagar ahora",
            "payTotal": "Pagar {total}",
            "completeOrder": "Completar pedido",
            "placingOrder": "Realizando pedido…",
            "creatingOrder": "Creando pedido…",
            "processingPayment": "Procesando pago…",
            "continueShopping": "Seguir comprando",
            "tryAgain": "Intentar de nuevo"
        },
        "errors": {
            "sessionExpiredTitle": "Sesión de compra expirada",
            "sessionExpiredMessage": "Este carrito ya no está disponible. Añade productos nuevamente.",
            "loadFailedTitle": "No se pudo cargar el pago",
            "loadFailedMessage": "Tuvimos problemas para cargar tu carrito. Por favor inténtalo de nuevo.",
            "orderNotFoundTitle": "Pedido no encontrado",
            "orderNotFoundMessage": "No pudimos encontrar este pedido.",
            "emailRequired": "El correo electrónico es obligatorio",
            "selectShippingAddress": "Por favor selecciona una dirección de envío",
            "selectShippingMethod": "Por favor selecciona un método de envío",
            "updateShippingMethodFailed": "Error al actualizar el método de envío",
            "orphanedCartMessage": "Este carrito está vinculado a una cuenta con sesión iniciada.",
            "orphanedCartBlocked": "Este carrito está vinculado a una cuenta.",
            "discountApplyFailed": "No se pudo aplicar este código de descuento.",
            "discountRemoveFailed": "Error al eliminar el código de descuento.",
            "invalidValue": "Valor no válido",
            "updateEmailFailed": "Error al actualizar el correo electrónico",
            "createAccountFailed": "Error al crear la cuenta",
            "updateAddressFailed": "Error al actualizar la dirección",
            "itemUnavailableTitle": "Un producto no está disponible",
            "itemUnavailableMessage": "Este producto no se puede enviar a la dirección ingresada.",
            "itemUnavailableRemoveMessage": "Este producto no se puede enviar. Elimínalo para continuar.",
            "itemUnavailableRemove": "Eliminar producto",
            "itemUnavailableRemoveFailed": "No se pudo eliminar el producto.",
            "fulfillmentCheckFailed": "No se pudo verificar la disponibilidad del producto.",
            "crashTitle": "Error en el pago",
            "crashMessage": "Algo salió mal al cargar el proceso de pago. Inténtalo de nuevo."
        },
        "contact": {
            "title": "Contacto",
            "haveAccount": "¿Tienes una cuenta?",
            "createAccountLabel": "Crear una cuenta para compras más rápidas",
            "activationNotice": "Después del pago, recibirás un correo electrónico para activar tu cuenta.",
            "guestCheckout": "Compra como invitado",
            "newCustomer": "¿Nuevo cliente?",
            "signInTitle": "Iniciar sesión",
            "resetPasswordTitle": "Restablecer tu contraseña",
            "resetPasswordSubtitle": "Ingresa una nueva contraseña para tu cuenta",
            "processing": "Procesando…",
            "passwordMinPlaceholder": "Contraseña (mínimo 8 caracteres)",
            "signedIn": "Sesión iniciada"
        },
        "summary": {
            "title": "Resumen del pedido",
            "show": "Mostrar",
            "hide": "Ocultar",
            "toggleOrderSummary": "{action} resumen del pedido",
            "itemCount": "{count, plural, one {# producto} other {# productos}}",
            "subtotal": "Subtotal",
            "shipping": "Envío",
            "taxVat": "Impuestos (IVA)",
            "discount": "Descuento",
            "total": "Total",
            "includingVat": "IVA incluido",
            "productFallback": "Producto",
            "soldOut": "Agotado",
            "unavailableHint": "Un producto no está disponible",
            "removeItem": "Eliminar",
            "contact": "Contacto",
            "shipTo": "Enviar a",
            "method": "Método",
            "delivery": "Entrega",
            "digital": "Digital"
        },
        "promo": {
            "placeholder": "Código de descuento",
            "apply": "Aplicar",
            "applying": "Aplicando…",
            "removeAriaLabel": "Eliminar código de descuento"
        },
        "shipping": {
            "methodTitle": "Método de envío",
            "loadingMethods": "Cargando métodos de envío…",
            "noAddressYet": "Por favor ingresa primero tu dirección de envío.",
            "addressTitle": "Dirección de envío",
            "countryRegion": "País / Región",
            "selectCountry": "Selecciona país",
            "backToSavedAddresses": "← Volver a direcciones guardadas",
            "emptySavedShipping": "No tienes direcciones guardadas. Ingresa tu dirección abajo.",
            "selectShippingAddressSheet": "Seleccionar dirección de envío"
        },
        "billing": {
            "title": "Dirección de facturación",
            "sameAsShipping": "Misma que la dirección de envío",
            "selectBillingSheet": "Seleccionar dirección de facturación",
            "emptySavedBilling": "No hay direcciones guardadas disponibles.",
            "backToSavedAddresses": "Volver a direcciones guardadas"
        },
        "addresses": {
            "selectPrompt": "Selecciona una dirección",
            "setDefaultShipping": "Guardar como dirección de envío predeterminada",
            "setDefaultBilling": "Guardar como dirección de facturación predeterminada",
            "defaultBadge": "Predeterminada",
            "emptySaved": "Aún no tienes direcciones guardadas."
        },
        "payment": {
            "totalUpdatedTitle": "El total de tu pedido fue actualizado",
            "totalUpdatedBody": "El total cambió de {previous} a {next}. Revisa el resumen antes de completar el pago.",
            "deliveryInvalidTitle": "El método de envío ya no está disponible",
            "deliveryInvalidBody": "Regresa al paso de envío y selecciona un método válido.",
            "completingTitle": "Procesando tu pedido",
            "completingBody": "Estamos confirmando tu pago y creando tu pedido. Esto tarda unos segundos, no cierres esta página.",
            "initFailed": "Error al inicializar el sistema de pago.",
            "unavailable": "El sistema de pago no está disponible temporalmente.",
            "loadingGateway": "Cargando pasarela de pago {gateway}…",
            "confirmingPayment": "Confirmando tu pago…",
            "securingWithStripe": "Asegurando tu pago. Esto suele tardar unos segundos.",
            "doNotClose": "Por favor no cierres ni recargues esta página.",
            "completeOrderFailed": "No se pudo completar tu pedido. Inténtalo de nuevo.",
            "placeOrderFailed": "No se pudo realizar el pedido. Contacta a soporte.",
            "totalsRefreshFailed": "No se pudieron actualizar los totales de compra.",
            "totalUnavailable": "Total no disponible. Recarga la página.",
            "currencyUnavailable": "Moneda no disponible. Recarga la página.",
            "validationFailed": "Error en la validación del pago",
            "methodRequired": "Elige una opción de pago e inténtalo de nuevo.",
            "detailsUnavailable": "No se pudieron obtener los detalles del pago.",
            "expressReset": "Los botones de pago rápido se reiniciaron.",
            "formReset": "El formulario de pago se reinició. Intenta pagar de nuevo.",
            "totalChanged": "El total del pedido cambió. Revisa el monto e intenta de nuevo.",
            "bankDeclined": "Tu banco rechazó el pago. Intenta con otra tarjeta.",
            "sessionExpired": "La sesión de pago expiró. Inténtalo de nuevo.",
            "channelUnresolved": "No se pudo resolver el canal de pago. Contacta a soporte.",
            "unexpectedError": "Ocurrió un error inesperado al completar el pago.",
            "stripeConfigFailed": "Error en la configuración de la pasarela Stripe",
            "stripeKeyMissing": "Falta la clave pública de Stripe en el panel de Saleor.",
            "dummyGateway": "Pago de Prueba",
            "failed": "Pago fallido",
            "interruptedBeforeCharge": "El pago fue interrumpido antes de realizar el cobro. Puedes intentarlo con seguridad.",
            "interruptedAfterAuthorize": "Tu pago fue procesado. Haz clic en 'Completar pedido' abajo.",
            "verificationUnavailable": "No pudimos verificar el intento de pago previo.",
            "authorizedTitle": "Pago autorizado — confirma tu pedido",
            "authorizedBody": "Tu pago ha sido autorizado. Toca abajo para confirmar tu pedido.",
            "freeOrderBody": "El total de tu pedido es {total}. No se requiere pago — confirma abajo.",
            "dummyTestMode": "Modo de prueba. No se requieren datos de tarjeta.",
            "stripeLoadTitle": "No se pudo cargar Stripe"
        },
        "confirmation": {
            "orderNumber": "Pedido #{number}",
            "thankYou": "¡Gracias por tu compra!",
            "statusTitle": "Estado del pedido",
            "confirmedTitle": "Tu pedido está confirmado",
            "publicTitle": "Tu pedido",
            "publicBody": "Los productos y totales se muestran aquí.",
            "confirmedEmail": "Recibirás un correo electrónico de confirmación en {email}",
            "emailSent": "Correo de confirmación enviado",
            "shippingAddress": "Dirección de envío",
            "billingAddress": "Ciudad de facturación",
            "shippingMethod": "Método de envío",
            "deliveryDays": "{days} días",
            "tracking": "Seguimiento",
            "createAccount": "Guardar este pedido en una cuenta",
            "signIn": "Iniciar sesión para ver todos los detalles del pedido"
        },
        "orderFind": {
            "title": "Buscar tu pedido",
            "body": "Ingresa el número de pedido de tu correo electrónico y la dirección que usaste.",
            "emailGateBody": "Confirma el correo utilizado en la compra.",
            "emailLabel": "Correo electrónico",
            "emailPlaceholder": "tu@ejemplo.com",
            "numberLabel": "Número de pedido",
            "numberPlaceholder": "Número de pedido",
            "confirmEmail": "Ver detalles del pedido",
            "submit": "Buscar pedido",
            "findAnother": "Buscar otro pedido",
            "generic": "No pudimos encontrar un pedido con esos datos.",
            "rateLimited": "Demasiados intentos. Inténtalo más tarde.",
            "lookupUnavailable": "Usa el enlace de tu correo de confirmación."
        },
        "server": {
            "marketingSaveFailed": "Error al guardar la preferencia de marketing",
            "invalidRedirectUrl": "URL de redirección no válida.",
            "createAccountFailed": "Error al crear la cuenta",
            "noSaleorResponse": "Sin respuesta de Saleor",
            "shippingMethodsFailed": "Error al cargar los métodos de envío",
            "gatewayInitFailed": "Error al inicializar la pasarela de pago",
            "totalVerifyFailed": "No se pudo verificar el total de la compra.",
            "totalChanged": "El total ha cambiado. Por favor revisa tu pedido.",
            "paymentInitFailed": "Error al inicializar el pago",
            "paymentsDisabled": "Los pagos no están habilitados en este entorno.",
            "paymentProcessFailed": "Error al procesar el pago",
            "completeOrderFailed": "Error al completar el pedido",
            "orderCreateFailed": "El pago fue procesado pero el pedido no se pudo crear.",
            "validationRulesUnavailable": "Reglas de validación no disponibles",
            "setDefaultAddressFailed": "Error al establecer la dirección predeterminada",
            "dummyNotAllowed": "El pago de prueba no está disponible en este entorno.",
            "stripeNotEnabled": "Los pagos con Stripe no están habilitados en este entorno."
        },
        "gateways": {
            "noneTitle": "No hay pasarela de pago configurada",
            "noneBody": "Para aceptar pagos, instala una aplicación de pago desde el Panel de Saleor.",
            "unsupportedTitle": "Pasarela de pago no compatible",
            "unsupportedList": "Esta compra no admite las pasarelas disponibles: {gateways}.",
            "unsupportedEmpty": "No hay pasarelas de pago disponibles para esta compra.",
            "dummyMissingTitle": "Pago de prueba no disponible",
            "dummyMissingBody": "Revisa la configuración de la aplicación de pago en el Panel de Saleor.",
            "noGatewayConfigured": "No hay pasarela de pago configurada.",
            "stripeUseCardForm": "El pago se gestiona mediante el formulario de tarjeta.",
            "paymentFailed": "Pago fallido",
            "paymentTryAgain": "El pago falló. Por favor inténtalo de nuevo.",
            "paymentWebhookFailed": "Error en el webhook de pago.",
            "paymentInitFailed": "No se pudo inicializar el pago."
        }
    }
}

with open("c:/Users/danil/Downloads/saleor-main/saleor-main/es.json", "w", encoding="utf-8") as f:
    json.dump(es, f, indent=2, ensure_ascii=False)

print("Generated es.json successfully!")
