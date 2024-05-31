/*
  Warnings:

  - You are about to drop the column `title` on the `Document` table. All the data in the column will be lost.
  - Added the required column `filename` to the `Document` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Document" DROP COLUMN "title",
ADD COLUMN     "fileSize" INTEGER NOT NULL DEFAULT 0,
ADD COLUMN     "filename" TEXT NOT NULL;
