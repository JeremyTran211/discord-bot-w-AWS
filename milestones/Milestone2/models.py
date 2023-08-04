"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""

from database import Database


class TestModel:
    """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.author = ctx.message.author.name

    def response(self):
        return f'Hi, {self.author}. I am alive'

class getCategory:
    def __init__(self, ctx, category):
        self.ctx = ctx
        self.category = category
     
       
    def getCategoryF(self):
        category_info = Database.getCategory(self.category) 
        return category_info

class findService:
    def __init__(self, ctx, service, location):
        self.ctx = ctx
        self.service = service
        self.location = location

       
    def findServiceF(self):
        service_info= Database.findService(self.service, self.location) 
        return service_info

class getRecord:
    def __init__(self, ctx, service, generator):
        self.ctx = ctx
        self.service = service
        self.generator = generator

       
    def getRecordF(self):
        record_info= Database.getRecord(self.service, self.generator) 
        return record_info

class getRegulation:
    def __init__(self, ctx, body):
        self.ctx = ctx
        self.body = body

    def getRegulationF(self):
        body_info = Database.getRegulation(self.body)
        return body_info

class addWaste:
    def __init__(self, ctx, category_name, category_desc, waste_categorycol, item_name, item_desc, item_quantity, generator_type):
        self.ctx = ctx
        self.category_name = category_name
        self.category_desc = category_desc
        self.waste_categorycol = waste_categorycol
        self.item_name = item_name
        self.item_desc = item_desc
        self.item_quantity = item_quantity
        self.generator_type = generator_type

    def addWasteF(self):
        return Database.addWaste(self.category_name, self.category_desc, self.waste_categorycol, self.item_name, self.item_desc, self.item_quantity, self.generator_type)

class AddSchedule:
  def __init__(self, ctx, schedule_title, schedule_description, account_id):
    self.ctx = ctx
    self.schedule_title = schedule_title
    self.schedule_description = schedule_description
    self.account_id = account_id

  def addScheduleF(self):
    Database.addSchedule(self.schedule_title, self.schedule_description, self.account_id)

class AddSchedule:
    def __init__(self, ctx, schedule_title, schedule_description, account_id):
        self.ctx = ctx
        self.schedule_title = schedule_title
        self.schedule_description = schedule_description
        self.account_id = account_id

    def addScheduleF(self):
        Database.addSchedule(self.schedule_title, self.schedule_description, self.account_id)

class UpdateProcess:
    def __init__(self, ctx, name, column, info):
        self.ctx = ctx
        self.name = name
        self.column = column
        self.info = info

    def updateProcessF(self):
        return Database.updateProcess(self.name, self.column, self.info)
      
class DeleteProvider:
    def __init__(self, ctx, service, name):
        self.ctx = ctx
        self.name = name
        self.service = service

    def deleteProviderF(self):
        return Database.deleteProvider(self.name, self.service)

class DeleteTech:
    def __init__(self, ctx, name):
        self.ctx = ctx
        self.name = name

    def deleteTechF(self):
        return Database.deleteTech(self.name)

class UpdateLog:
    def __init__(self, ctx, log_ID, column, new_info):
        self.ctx = ctx
        self.log_ID = log_ID
        self.column = column
        self.new_info = new_info

    def updateLogF(self):
        Database.addTriggerLogs()
        return Database.updateLog(self.log_ID, self.column, self.new_info)

class UpdateRecord:
    def __init__(self, ctx, record_Type, column, info):
        self.ctx = ctx
        self.record_Type = record_Type
        self.column = column
        self.info = info

    def updateRecordF(self):
        Database.addTrigger()
        return Database.updateRecord(self.record_Type, self.column, self.info)

class ItemSummary:
    def __init__(self, ctx, category_name):
        self.ctx = ctx
        self.category_name = category_name

    def getItemSummary(self):
        Database.addProcedure()  
        return Database.getSummary(self.category_name)

class UpdateService:
    def __init__(self,ctx, table, row, column, info):
        self.ctx = ctx
        self.table = table
        self.row = row
        self.column = column
        self.info = info

    def updateServiceF(self):
        return Database.updateService(self.table, self.row, self.column, self.info)
