from mysql.connector import Error
from connection import connectionMZ, disconnection
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/mazatlan",
    tags=["mazatlan"],
    responses={404: {"description": "Not found"}})

@router.get("/")
def getCalls():
    connect, cursor = connectionMZ()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr;")
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
    connect, cursor = connectionMZ()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where (DATE(calldate) >= %s and DATE(calldate) <= %s);")
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
    connect, cursor = connectionMZ()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where src = %s;")
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
    connect, cursor = connectionMZ()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where dst = %s;")
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
    connect, cursor = connectionMZ()
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
    connect, cursor = connectionMZ()
    try:
        query = ("select calldate, src, dst, duration, disposition from cdr where disposition = %s;")
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