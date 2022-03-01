import sqlite3
import pandas as pd

cnx_old = sqlite3.connect("oc-lettings-site-old.sqlite3")
cnx_new = sqlite3.connect("oc-lettings.sqlite3")


df_user = pd.read_sql("SELECT * FROM auth_user", cnx_old)
df_user.to_sql("auth_user", cnx_new, if_exists="replace")

df_adress = pd.read_sql("SELECT * FROM oc_lettings_site_address", cnx_old)
df_adress.to_sql("lettings_address", cnx_new, if_exists="replace")

df_letting = pd.read_sql("SELECT * FROM oc_lettings_site_letting", cnx_old)
df_letting.to_sql("lettings_letting", cnx_new, if_exists="replace")

df_profile = pd.read_sql("SELECT * FROM oc_lettings_site_profile", cnx_old)
df_profile.to_sql("profiles_profile", cnx_new, if_exists="replace")
