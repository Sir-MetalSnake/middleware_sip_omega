from mysql.connector import Error
from connection import connection, disconnection
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/losmochis",
    tags=["losmochis"],
    responses={404: {"description": "Not found"}})


@router.get("/")
def getCalls():
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr WHERE src LIKE '10%' or dst LIKE '10%';")
        cursor.execute(query)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/bydate")
def getDate(startDate, endDate):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where (calldate between %s and %s) and (src LIKE '10%' or dst LIKE '10%');")
        val = (startDate, endDate,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/bySrc")
def getSrc(src):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where (src = %s) and (src LIKE '10%' or dst LIKE '10%') ;")
        val = (src,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/byDst")
def getDst(dst):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where (dst = %s) and and (src LIKE '10%' or dst LIKE '10%');")
        val = (dst,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/bySrcDst")
def getSrcDst(src,dst):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where src = %s and dst = %s ;")
        val = (src, dst,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)


@router.get("/byStatus")
def getStatus(status):
    connect, cursor = connection()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where (disposition = %s) and (src LIKE '10%' or dst LIKE '10%');")
        val = (status,)
        cursor.execute(query, val)
        records = cursor.fetchall()

        if records:
            calls_list = []
            for record in records:
                date, source, destination, duration, status = record
                fecha_hora = datetime.fromisoformat(str(date))
                fecha = fecha_hora.date()
                hora = fecha_hora.time()
                call_dict = {
                    "calldate": str(fecha) + " " + str(hora),
                    "src": source,
                    "dst": destination,
                    "duration": duration,
                    "status": status
                }
                calls_list.append(call_dict)

            return {"Calls": calls_list}
    except Error as e:
        return {"Error: ", e}
    finally:
        disconnection(connect, cursor)