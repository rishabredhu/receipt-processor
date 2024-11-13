from fastapi import APIRouter, HTTPException
from app.api.schemas import Receipt, ReceiptResponse, PointsResponse
from app.store.memory import store
from app.services.points import calculate_points






router = APIRouter()

@router.post("/receipts/process", response_model=ReceiptResponse)
async def process_receipt(receipt: Receipt):
    receipt_id = store.save_receipt(receipt)
    return ReceiptResponse(id=receipt_id)

@router.get("/receipts/{id}/points", response_model=PointsResponse)
async def get_points(id: str):
    receipt = store.get_receipt(id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    points = calculate_points(receipt)
    return PointsResponse(points=points)
