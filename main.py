import flet as ft
import os
import traceback
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

supabase = None
if supabase_url and supabase_key:
    try:
        from supabase import create_client, Client
        supabase = create_client(supabase_url, supabase_key)
    except Exception as e:
        print("Error inicializando Supabase:", e)


def main(page: ft.Page):
    page.title = "Registro Escuela - Autenticación"
    page.window_width = 800
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def show_snack(message, color=ft.Colors.RED_400):
        try:
            snack = ft.SnackBar(content=ft.Text(message), bgcolor=color)
            page.overlay.append(snack)
            snack.open = True
            page.update()
        except:
            page.snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor=color)
            page.snack_bar.open = True
            page.update()

    def go_login(e=None):
        page.controls.clear()
        page.add(login_view())
        page.update()

    def go_register(e=None):
        page.controls.clear()
        page.add(register_view())
        page.update()

    def login_view():
        txt_usu = ft.TextField(label="Usuario", width=300, prefix_icon="person")
        txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, prefix_icon="lock")
        
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
                else:
                    show_snack("Credenciales incorrectas")
            except Exception as ex:
                show_snack(f"Error BD: {ex}")

        return ft.Column(
            [
                ft.Text("Iniciar Sesión", size=32, weight=ft.FontWeight.BOLD),
                txt_usu,
                txt_pass,
                ft.Container(height=10),
                ft.ElevatedButton("Ingresar", icon="login", on_click=on_login_click),
                ft.TextButton("¿No tienes cuenta? Regístrate aquí", on_click=go_register)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def register_view():
        txt_name = ft.TextField(label="Nombre Completo", width=300, prefix_icon="badge")
        txt_usu = ft.TextField(label="Nombre de Usuario", width=300, prefix_icon="person")
        txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, prefix_icon="lock")

        def on_register_click(e):
            if not txt_name.value or not txt_usu.value or not txt_pass.value:
                show_snack("Por favor llena todos los campos")
                return
            if not supabase:
                show_snack("Sin conexión a BD", ft.Colors.ORANGE_500)
                return
            try:
                data = {"name": txt_name.value, "nameUsu": txt_usu.value, "pass": txt_pass.value, "role": 1}
                supabase.table("usuarios").insert(data).execute()
                show_snack("Registrado exitosamente", ft.Colors.GREEN_500)
                go_login()
            except Exception as ex:
                show_snack(f"Error al registrar: {ex}")

        return ft.Column(
            [
                ft.Text("Registro", size=32, weight=ft.FontWeight.BOLD),
                txt_name,
                txt_usu,
                txt_pass,
                ft.Container(height=10),
                ft.ElevatedButton("Registrarse", icon="person_add", on_click=on_register_click),
                ft.TextButton("Regresar a Iniciar Sesión", on_click=go_login)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # El método directo que jamás falla para mostrar elementos
    go_login()

if __name__ == "__main__":
    try:
        # Algunos forks usan run() y app() lanza un warning
        if hasattr(ft, "run"):
            ft.run(main)
        else:
            ft.app(target=main)
    except:
        ft.app(target=main)
