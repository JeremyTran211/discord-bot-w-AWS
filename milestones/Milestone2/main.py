"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
from database import Database as db
from discord.ext import commands
from model import *

TOKEN='MTEzMTQ2NzY3Njg3MTU1NzE0Mg.GLelwf.eDTfxoOOwtIE8rhWe48gEI4kewcry5QEEb970U'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event 
async def on_ready(): 
    # everything in this method executes automatically when the bot is put online 
    print(f"{bot.user.name} joined the room")
    # you need to import the file database.py as db for the next lines to work
    if db.connect(): 
             print(f"{bot.user.name} is connected to the remote database")
    else: 
             print(f"{bot.user.name} was unable to connect to the remote database")

@bot.command(name="test", description="write your database business requirement for this command here")
async def _test(ctx):
    testModel = TestModel(ctx)
    response = testModel.response()
    await ctx.send(response)

# TODO: complete the following tasks:
#       (1) Replace the commands' names with your own commands
#       (2) Write the description of your business requirement in the description parameter
#       (3) Implement your commands' methods.

@bot.command(name="GetCategory", description="For each waste category, find the amount of waste produced by individuals, businesses  or both along with the top waste item of that category.")
async def GetCategory(ctx, category): #function name and parameters
    getCategoryObj = getCategory(ctx, category)
    results = getCategoryObj.getCategoryF()

    if results is None or len(results) == 0:
        await ctx.send(f"No results found for category: {category}.")
        return

    response = f"{category}:\n"
    for result in results:
        response += f"Generator: {result['generator_Type']}\n Item: {result['item_Name']}\n Quantity: {result['total_quantity']}\n"
    await ctx.send(response)


@bot.command(name="FindService", description="For each service provider, provide users infomation based on service type and location.")
async def FindService(ctx, *, args):
    args = args.split('" ')
    if len(args) < 2:
        await ctx.send("You must provide two arguments.")
        return
    service = args[0].replace('"', '')
    location = args[1].replace('"', '')
    findServiceObj = findService(ctx, service, location)
    result = findServiceObj.findServiceF()
    
    if result is None or len(result) == 0:
        await ctx.send(f"No results found for service: {service}.")
        return

    response = f"Service: {service}\n"
    for i, info in enumerate(result):
        response += f"Name: {info['Name']},\nInformation: {info['Information']}\n"
    await ctx.send(response)


@bot.command(name="GetRecord", description="For each records, find the average cost within area X for service type Y.")
async def GetRecord(ctx, *,args):
   args = args.split('" ')
   if len(args) < 2:
        await ctx.send("You must provide two arguments.")
        return
   service = args[0].replace('"', '')
   generator = args[1].replace('"', '')
   getRecordObj = getRecord(ctx, service, generator)
   result = getRecordObj.getRecordF()
  
   if result is None or len(result) == 0:
        await ctx.send(f"No results found for service or generator")
        return 

   for record in result:
       record_message = f"Generator: {record['generator_Type']}\nService: {record['service_Type']}\nRecord Type: {record['record_Type']}\nAverage: {record['Recordscol']}"
       await ctx.send(record_message)

@bot.command(name="RegulatoryBody", description="For each regulator body, find X amount of regulations they created")
async def RegulatoryBody(ctx, body):
    getRegulationObj = getRegulation(ctx, body)
    result = getRegulationObj.getRegulationF()
    
    if result is None or len(result) == 0:
        await ctx.send(f"No regulations found for body: {body}")
        return 

    for index, regulation in enumerate(result, start=1):
        regulation_message = f"{index}. Title: {regulation['regulation_Title']}\n Description: {regulation['regulation_Description']}"
        await ctx.send(regulation_message)                    
 

           
@bot.command(name="AddWaste", description="Users shall be able to update the waste category and item without having to repeat infomation")
async def AddWaste(ctx, category_name, category_desc, waste_categorycol, item_name, item_desc, item_quantity, generator_type):
    addWasteObj = addWaste(ctx, category_name, category_desc, waste_categorycol, item_name, item_desc, item_quantity, generator_type)
    success = addWasteObj.addWasteF()
    if success:
        await ctx.send("Record added successfully.")
    else:
        await ctx.send("An error occurred while adding the record.")

@bot.command(name="AddSchedule", description="Individual users or businesses can create collection schedule that will be based on service providers.")
async def AddScehdule(ctx, *,args):
    args = args.split('" ')
    if len(args) < 3:
        await ctx.send("You must provide three arguments.")
        return
    schedule_title = args[0].replace('"', '')
    schedule_description = args[1].replace('"', '')
    account_id = args[2].replace('"', '')

    addScehduleObj = AddSchedule(ctx, schedule_title, schedule_description, account_id)
    addScehduleObj.addScheduleF()

    await ctx.send("Schedule has been added successfully!")


@bot.command(name="UpdateService", description="If a service provider infomation changes, that change shall be reflected in the database.")
async def updateService(ctx, table, row, column, *args):
    info = ' '.join(args) 
    service = UpdateService(ctx, table, row, column, info)
    result = service.updateServiceF()

    if result:
        await ctx.send(f"Service '{row}' was updated successfully in table '{table}'.")
    else:
        await ctx.send("An error occurred while trying to update the service.")



@bot.command(name="UpdateProcess", description="If a treatment process has any updates or changes to it, the update shall be reflected in the database.")
async def updateProcess(ctx, name, column, *args):
    info = ' '.join(args)
    UpdateProcessObj = UpdateProcess(ctx, name, column, info)
    result = UpdateProcessObj.updateProcessF()
  
    if result:
        await ctx.send(f"Process {name} has been successfully updated.")
    else:
        await ctx.send("An error occurred while updating the process.")

@bot.command(name="DeleteProvider", description="If service provider is no longer in business, their infomation will be deleted from the database.")
async def deleteProvider(ctx, service_type, name):
    deleteProviderObj = DeleteProvider(ctx, service_type, name)
    result = deleteProviderObj.deleteProviderF()
  
    if result:
        await ctx.send(f"The provider {name} has been successfully deleted.")
    else:
        await ctx.send("An error occurred while deleting the provider.")


@bot.command(name="DeleteTech", description="If a waste technology is no longer relevant to the industry and needs to be removed, the database shall support that and remove it from treatment process.")
async def deleteTech(ctx, name):
    deleteTechObj = DeleteTech(ctx, name)
    result = deleteTechObj.deleteTechF()
    
    if result:
        await ctx.send(f"The technology '{name}' has been successfully deleted.")
    else:
        await ctx.send("An error occurred during deletion. Please try again.")

@bot.command(name="UpdateLog", description="If a user updates their log, then there will be a trigger that updates the current time of log.")
async def updateLog(ctx, log_ID: int, column: str, new_info: str):
    updateLogObj = UpdateLog(ctx, log_ID, column, new_info)
    result = updateLogObj.updateLogF()
    
    if result is not None:
        await ctx.send(f"Log ID: {result[0]} has been updated. Its new current time is {result[1]}.")
    else:
        await ctx.send("There was an error updating the log.")

@bot.command(name="UpdateRecord", description="If there is an update in the records, the time will automatically update and user will be able to see which one updated and the time.")
async def updateRecord(ctx, record_Type: str, column: str, new_info: str):
    record = UpdateRecord(ctx, record_Type, column, new_info)
    result = record.updateRecordF()
    if result is not None:
        await ctx.send(f"Record '{result[0]}' updated. New timestamp is {result[1]}")
    else:
        await ctx.send("An error occurred while trying to update the record.")

@bot.command(name="GetQuarterSummary", description="There will be a stored procedure that generates a summary of the waste collected in a given quarter broken down by waste category, item within that category and generator.")
async def getQuarterSummary(ctx,category):
    summaryObj =  ItemSummary(ctx, category)
    summary = Database.getItemSummary(category)  
    if summary is not None:
        await ctx.send(f"Summary for {quarter}:\n{summary}")
    else:
        await ctx.send("An error occured")

@bot.command(name="cmd_13", description="database business requirement #13 here")
async def _command13(ctx, *args):
    await ctx.send("This method is not implemented yet")


@bot.command(name="cmd_14", description="database business requirement #14 here")
async def _command14(ctx, *args):
    await ctx.send("This method is not implemented yet")

bot.run(TOKEN)
