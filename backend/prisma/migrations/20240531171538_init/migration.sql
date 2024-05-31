-- CreateTable
CREATE TABLE "Document" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "createdDate" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Document_pkey" PRIMARY KEY ("id")
);
