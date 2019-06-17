# Project LUAD

---
## 1.Epigenome - DNA methylation Analysis

### 1-1. Preprocessing Sequencing Reads
We ran Trimmomatic verision 0.33 to trim low quality bases and adapter contaminated reads.
```
java -jar trimmomatic-0.33.jar PE -phred33 read1.fastq read2.fastq read1_paired.fastq read1_unpaired.fastq read2_paired.fastq read2_unpaired.fastq ILLUMINACLIP:TruSeq2-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30
```
### 1-2. Read Alignment, deduplication and extraction of DNA methylation info
We performed read alignment, deduplication and DNA methylation calculation via using Bismark version 0.14.3
```
<Alignment>
bismark --bowtie2 -1 read1_paired.fastq -2 read2_paired.fastq
<Deduplication>
deduplicate_bismark sample.bam 
<Methylation Extraction>
bismark_methylation_extractor -p --mbias_off --no_overlap --counts --bedGraph --no_header --cytosine_report sample.bam
```
We then integrated Watson and Crick Strand CpG methylation Coverage from sample_deduplicated.CpG_report.txt

test [fdafdsfsdf]

## 2.Transcriptome - RNA-seq Analysis

### 2-1. Preprocessing Sequencing Reads


## 3. Exome - Exome-seq Analysis

### 3-1. Preprocessing Sequencing Reads

## 4. Data Integration

```
hello hello this is a test fuckfuck
```
