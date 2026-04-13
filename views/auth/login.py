import flet as ft
from core.database import get_supabase_client

def get_login_view(page: ft.Page):
    supabase = get_supabase_client()
    
    txt_usu = ft.TextField(label="Usuario", width=300, prefix_icon="person")
    txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, prefix_icon="lock")
    
    def show_snack(message, color=ft.Colors.RED_400):
        snack = ft.SnackBar(content=ft.Text(message), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def on_login_click(e):
        if not txt_usu.value or not txt_pass.value:
            show_snack("Por favor llena todos los campos")
            return
        if not supabase:
            show_snack("Sin conexión a BD", ft.Colors.ORANGE_500)
            return
        try:
            res = supabase.table("usuarios").select("*").eq("nameUsu", txt_usu.value).eq("pass", txt_pass.value).execute()
            if res.data and len(res.data) > 0:
                show_snack(f"¡Bienvenido {res.data[0].get('name')}!", ft.Colors.GREEN_500)
                # Redirect to dashboard upon successful login
                page.go("/dashboard")
            else:
                show_snack("Credenciales incorrectas")
        except Exception as ex:
            show_snack(f"Error BD: {ex}")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Iniciar Sesión", size=32, weight=ft.FontWeight.BOLD),
                txt_usu,
                txt_pass,
                ft.Container(height=10),
                ft.ElevatedButton("Ingresar", icon="login", on_click=on_login_click),
                ft.TextButton("¿No tienes cuenta? Regístrate aquí", on_click=lambda e: page.go("/register"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.Alignment.CENTER,
        expand=True
    )
