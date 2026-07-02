from pydantic import BaseModel, Field

class CompanyAnalysisRequest(BaseModel):

    company_name: str = Field(..., min_length=1, description="분석할 회사명. 예: Apple, Tesla")