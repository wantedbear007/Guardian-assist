from prisma import Prisma

# logging uploaded file to database
async def register_pdf(filename: str, filesize: int = 0):
    prisma = Prisma()
    try:
        await prisma.connect();
        await prisma.document.create(
            data={
                'filename':filename,
            }
        )
    except Exception as e:
        print(f"error occurred {e}")
        
    finally:
        await prisma.disconnect();