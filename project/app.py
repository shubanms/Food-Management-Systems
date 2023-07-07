from flask import Flask, render_template, request, redirect, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# PostgreSQL database configuration
db_config = {
    "host": "localhost",
    "database": "FoodManagementSystem",
    "user": "postgres",
    "password": "YOUR_PASSWORD"
}

# Admin credentials
admin_username = 'admin'
admin_password = 'password'


def connect_to_database():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")


@app.route('/')
def home():
    if 'admin' in session and session['admin']:
        return redirect('/dashboard')
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == admin_username and password == admin_password:
        session['admin'] = True
        return redirect('/dashboard')
    else:
        return render_template('login.html', error=True)


@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    if 'admin' in session and session['admin']:
        return render_template('dashboard.html')
    return redirect('/')


@app.route('/order-details', methods=['GET', 'POST'])
def order_details():
    if 'admin' not in session or not session['admin']:
        return redirect('/')

    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        customer_name = request.form.get('customer_name')

        conn = connect_to_database()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT o.order_id, o.order_date, o.total_amount, c.customer_name, c.address, c.city, c.state, c.country
                FROM ORDERS o
                JOIN CUSTOMERS c ON o.customer_id = c.customer_id
                WHERE c.customer_id = %s AND c.customer_name = %s
            """, (customer_id, customer_name))
            order_details = cursor.fetchall()
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error retrieving order details: {e}")
            conn.rollback()
            return render_template('order_form.html', error_message="Error retrieving order details. Please try again.")
        finally:
            cursor.close()
            conn.close()

        return render_template('order_details.html', order_details=order_details)

    return render_template('order_form.html')


@app.route('/update-feedback', methods=['GET', 'POST'])
def update_feedback():
    if 'admin' not in session or not session['admin']:
        return redirect('/')

    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        feedback_text = request.form.get('feedback_text')

        conn = connect_to_database()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE FEEDBACK
                SET feedback_text = %s
                WHERE customer_id = %s
            """, (feedback_text, customer_id))
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error updating feedback: {e}")
            conn.rollback()
            return render_template('feedback_form.html', error_message="Error updating feedback. Please try again.")
        finally:
            cursor.close()
            conn.close()

        return render_template('update_feedback.html', success_message="Feedback updated successfully.")

    return render_template('feedback_form.html')


@app.route('/view-table', methods=['GET', 'POST'])
def view_table():
    if 'admin' not in session or not session['admin']:
        return redirect('/')

    if request.method == 'POST':
        table_name = request.form.get('table_name')

        conn = connect_to_database()
        cursor = conn.cursor()

        try:
            # Get table description
            cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
            table_description = cursor.fetchall()

            # Get top 5 rows from the table
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
            table_rows = cursor.fetchall()

            conn.commit()
        except psycopg2.Error as e:
            print(f"Error retrieving table data: {e}")
            conn.rollback()
            return render_template('view_table.html', error_message="Error retrieving table data. Please try again.")
        finally:
            cursor.close()
            conn.close()

        return render_template('view_table.html', table_name=table_name, table_description=table_description,
                               table_rows=table_rows)

    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        # Get all table names from the database
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_names = cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Error retrieving table names: {e}")
        return render_template('view_table.html', error_message="Error retrieving table names. Please try again.")
    finally:
        cursor.close()
        conn.close()

    return render_template('view_table.html', table_names=table_names)


if __name__ == '__main__':
    app.run(debug=True)
    
    
