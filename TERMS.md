# TERMS – Chat Stream Real‑Time Summarizer

## Good or Service Description
A Python 3.11 prototype that:
1. Streams plain‑text chat at ≥20 msgs · s⁻¹.
2. Buckets by sliding five‑second windows and semantic topic vectors.
3. Sends each bucket to two hot‑swappable models  
   • Sentiment classifier (RoBERTa‑tiny or local DistilBERT).  
   • Summarizer (Long‑T5 small or OpenAI gpt‑3.5‑turbo‑16k via optional cloud flag).  
4. Produces snapshots: sentiment bar (+/–/neutral), 2‑sentence abstract, 0‑1 confidence score.  
5. Aggregates snapshots fractally (window → minute → hour) without O(n²) growth.

## Scope of Work
Implement streaming loop, model wrappers, config‑driven scaling tree, on‑disk and Redis back‑pressure buffer, and evaluation script measuring throughput, latency, and ROUGE‑L vs. human summaries.

## Duration & Milestones
Total 16 weeks from contract date.  
1. Week 4 – design doc + data schema.  
2. Week 8 – end‑to‑end loop hitting 10 msgs · s⁻¹ on laptop.  
3. Week 12 – latency <200 ms at 20 msgs · s⁻¹ on 8‑vCPU VM.  
4. Week 16 – doc, unit tests, benchmark report, Dockerfile.

## Payment Terms
22 000 USDT, one tranche released 14 days after milestone 4 acceptance.

## Delay & Extension
Penalty 2 % of unpaid amount per full week late beyond week 16.  
Creator may grant up to 4 weeks extension if ≥75 % of tests already pass.

## Confidentiality
Code public; proprietary model API keys redacted.

## Dispute Resolution
Arbiter verifies Git history, CI logs, and benchmarks in `submissions/`.

## Appendices
A. Recommended models & hardware tables.  
B. Benchmark methodology. :contentReference[oaicite:1]{index=1}
