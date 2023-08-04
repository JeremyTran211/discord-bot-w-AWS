# In this file you must implement your main query methods 
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

# note that your remote host where your database is hosted
# must support user permissions to run stored triggers, procedures and functions.
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class Database:

    @staticmethod
    def connect():
        """
        This method creates a connection with your database
        IMPORTANT: all the environment variables must be set correctly
                   before attempting to run this method. Otherwise, it
                   will throw an error message stating that the attempt
                   to connect to your database failed.
        """
        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            print("Bot connected to database {}".format(db_name))
            return conn
        except:
            print("Bot failed to create a connection with your database because your secret environment variables " +
                  "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
            print("\n")

    @staticmethod
    def getCategory(category):
      try: 
        connected = Database.connect();
        if connected:
          with connected.cursor() as cursor:
            sql = """ SELECT i.generator_Type, i.item_Name, SUM(i.item_quantity) as total_quantity
                      FROM Waste_Item i
                      JOIN Waste_Category c ON i.item_Name = c.item_Name
                      WHERE c.category_Name = %s   
                      GROUP BY i.generator_Type, i.item_Name
                      ORDER BY total_quantity DESC
                  """
            cursor.execute(sql, (category))
            result = cursor.fetchall()
            return result
      except Exception as e:
        print("An error occurred:", e)
        return None  
        
    @staticmethod
    def findService(service, location):
      try: 
        connected = Database.connect();
        if connected:
          with connected.cursor() as cursor:
            sql = """ SELECT RC.Information, RC.Name 
                      FROM Recycling_Center RC
                      INNER JOIN Service_Providers SP
                      ON RC.service_Type = SP.service_Type
                      WHERE SP.service_Type = %s AND RC.Location = %s
                      UNION ALL
                      SELECT TC.Information, TC.Name 
                      FROM Treatment_Facility TC
                      INNER JOIN Service_Providers SP
                      ON TC.service_Type = SP.service_Type
                      WHERE SP.service_Type = %s AND TC.Location = %s
                      UNION ALL
                      SELECT WD.Information, WD.Name 
                      FROM Waste_Disposal_Site WD
                      INNER JOIN Service_Providers SP
                      ON WD.service_Type = SP.service_Type
                      WHERE SP.service_Type = %s AND WD.Location = %s
                      UNION ALL
                      SELECT WT.Information, WT.Name 
                      FROM Waste_Transporter WT
                      INNER JOIN Service_Providers SP
                      ON WT.service_Type = SP.service_Type
                      WHERE SP.service_Type = %s AND WT.Location = %s
                  """
            cursor.execute(sql, (service, location, service, location, service, location, service, location))
            result = cursor.fetchall()
            return result
      except Exception as e:
        print("An error occurred:", e)
        return None  

    @staticmethod
    def getRecord(service, generator):
        try: 
            connected = Database.connect();
            if connected:
                with connected.cursor() as cursor:
                    sql = """ SELECT generator_Type, service_Type, Recordscol, record_Type
                              FROM Records
                              WHERE  service_Type = %s AND  generator_Type = %s
                          """
                    cursor.execute(sql, (service, generator))
                    result = cursor.fetchall()
                    return result
        except Exception as e:
            print("An error occurred:", e)
            return None

    @staticmethod
    def getRegulation(body):
       try: 
            connected = Database.connect();
            if connected:
                with connected.cursor() as cursor:
                    sql = """ SELECT R.regulation_Title, R.regulation_Description
                              FROM Regulation R
                              INNER JOIN Regulatory_Body RB 
                              ON R.body_ID = RB.body_ID
                              WHERE RB.body_Name = %s
                          """
                    cursor.execute(sql, (body))
                    result = cursor.fetchall()
                    return result
       except Exception as e:
          print("An error occurred:", e)
          return None

    @staticmethod
    def addWaste(category_name, category_desc, waste_categorycol, item_name, item_desc, item_quantity, generator_type):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
                  
                  sql_item = """INSERT INTO Waste_Item(item_Name, item_Description, item_Quantity, generator_Type)
                                VALUES(%s, %s, %s, %s)
                             """
                  cursor.execute(sql_item, (item_name, item_desc, item_quantity, generator_type))
          
                  sql_category = """INSERT INTO Waste_Category(category_Name, category_Description, Waste_Categorycol, item_Name)
                                   VALUES(%s, %s, %s, %s)
                                """
                  cursor.execute(sql_category, (category_name, category_desc, waste_categorycol, item_name))
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def addSchedule(title, desc, accID):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
    
                  sql = """INSERT INTO Collection_Schedule(schedule_Title, schedule_description, account_ID) 
                           SELECT %s, %s, account_ID 
                           FROM Account 
                           WHERE account_ID = %s;
                        """
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def updateService(table_name, row_name, column_to_update, new_info):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
    
                  sql = f"UPDATE {table_name} SET {column_to_update} = %s WHERE Name = %s"
                      
                  cursor.execute(sql, (new_info, row_name))
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def updateProcess(name, column, new_info):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
    
                  sql = f"UPDATE Treatment_Process SET {column} = %s WHERE process_Name = %s"
                
                  cursor.execute(sql, (new_info, name))
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def deleteProvider(service, name):
      tables = ['Recycling_Center', 'Treatment_Facility', 'Waste_Transporter', 'Waste_Disposal_Site']
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
  
                  for table in tables:
                      sql = "DELETE FROM " + table + " WHERE Name = %s AND service_Type = %s"
                      cursor.execute(sql, (name, service))
  
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def deleteTech(name):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")

                  #check that the tech exist
                  sql_check = "SELECT * FROM Treatment_Technology WHERE tech_Name = %s"
                  cursor.execute(sql_check, (name,))
                  result = cursor.fetchone()

                
                  if result is None:
                    print("The technology does not exist.")
                    cursor.execute("ROLLBACK")
                    return False
                  
                  sql_update = "UPDATE Treatment_Process SET tech_Name = NULL WHERE tech_Name = %s"
                  cursor.execute(sql_update, (name))
  
                  sql_delete = "DELETE FROM Treatment_Technology WHERE tech_Name = %s"
                  cursor.execute(sql_delete, (name))
    
                  cursor.execute("COMMIT")
      except Exception as e:
          print("An error occurred:", e)
          if connected:
              connected.rollback()
          return None
      return True

    @staticmethod
    def updateLog(log_ID, column, new_info):
      try:
        connected = Database.connect()
        if connected:
            with connected.cursor() as cursor:
                cursor.execute("START TRANSACTION")

                # Update the specified column of the log
                sql_update = f"UPDATE Waste_Logs SET {column} = %s WHERE log_ID = %s"
                cursor.execute(sql_update, (new_info, log_ID))

                # Get the updated timestamp
                sql_select = "SELECT log_Timestamp FROM Waste_Logs WHERE log_ID = %s"
                cursor.execute(sql_select, (log_ID,))
                result = cursor.fetchone()

                cursor.execute("COMMIT")

                if result:
                  return log_ID, result['log_Timestamp']
                else:
                  return log_ID, None
                  
      except Exception as e:
        print("An error occurred:", e, type(e).__name__)
        if connected:
            connected.rollback()
        return None
        
# I get a privilege error and have tried multiple methods to fix it. Decided to add it to my python code so my sql code doesn't throw an error. 
# I have attached all the procedure and triggers to this file to show my triggers and procedure logic.
# "An error occurred: (1419, 'You do not have the SUPER privilege and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)')"      
    @staticmethod
    def addTriggerLOG():
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
  
                  sql_create_trigger = """
                      CREATE TRIGGER update_LOG_Timestamp 
                      BEFORE UPDATE ON Waste_Logs
                      FOR EACH ROW 
                      SET NEW.log_Date = NOW();
                  """
                  cursor.execute(sql_create_trigger)
  
                  cursor.execute("COMMIT")
                  print("Trigger created successfully.")
                  return True
  
      except Exception as e:
        print("An error occurred:", e)
        if connected:
            connected.rollback()
        return False  
        
    @staticmethod
    def updateRecord(record_Type, column, info):
      try:
        connected = Database.connect()
        if connected:
            with connected.cursor() as cursor:
                cursor.execute("START TRANSACTION")
    
                sql_update = f"UPDATE Records SET {column} = %s WHERE record_Type = %s"
                cursor.execute(sql_update, (info, record_Type))
    
                sql_select = "SELECT record_Date FROM Records WHERE record_Type = %s"
                cursor.execute(sql_select, (record_Type,))
                result = cursor.fetchone()
    
                cursor.execute("COMMIT")
    
                if result:
                    return record_Type, result['record_Date']
                else:
                    return record_Type, None  
    
      except Exception as e:
        print("An error occurred:", e)
        if connected:
            connected.rollback()
        return None
    
    @staticmethod
    def addTrigger():
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.execute("START TRANSACTION")
  
                  sql_create_trigger = """
                      CREATE TRIGGER update_Record_Timestamp 
                      BEFORE UPDATE ON Records 
                      FOR EACH ROW 
                      SET NEW.record_Date = NOW();
                  """
                  cursor.execute(sql_create_trigger)
  
                  cursor.execute("COMMIT")
                  return True
  
      except Exception as e:
        print("An error occurred:", e)
        if connected:
            connected.rollback()
        return False  
        
    @staticmethod
    def get_item_details(category_name):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.callproc('GetItemDetails', [category_name])
                  result = cursor.fetchall()
                  return result
      except Exception as e:
          print("An error occurred:", e)
          return None

    @staticmethod
    def addProcedure():
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
  
                  sql_create_trigger = """
                                            CREATE PROCEDURE GetItemDetails(IN p_category_name VARCHAR(45))
                                            BEGIN
                                              SELECT 
                                                  wi.item_Name,
                                                  wi.item_Quantity,
                                                  wg.generator_Type,
                                                  wg.Location,
                                                  wg.generator_Description
                                              FROM 
                                                  Waste_Category wc 
                                              INNER JOIN 
                                                  Waste_Item wi ON wc.item_Name = wi.item_Name 
                                              INNER JOIN 
                                                  Waste_Generator wg ON wi.generator_Type = wg.generator_Type
                                              WHERE 
                                                  wc.category_Name = p_category_name;
                                          """
                  cursor.execute(sql_create_trigger)
                  return True
  
      except Exception as e:
        print("An error occurred:", e)
        if connected:
            connected.rollback()
        return False  
        
    @staticmethod
    def getSummary(category_name):
      try:
          connected = Database.connect()
          if connected:
              with connected.cursor() as cursor:
                  cursor.callproc('GetItemDetails', [category_name])
                  result = cursor.fetchall()
                  return result
      except Exception as e:
          print("An error occurred:", e)
          return None
